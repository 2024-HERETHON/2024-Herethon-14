from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.conf import settings
#장고에서 기본적으로 제공해주는 유저 커스텀해서 만드는거

class UserManager(BaseUserManager):

    def create_user(self,username, email, password=None):
        if not username:
            raise ValueError('아이디좀 입력해주세요')
        user = self.model(
            username=username,
            email=self.normalize_email(email),
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

#슈퍼유저 만드는거
    def create_superuser(self,username, email, password):
        user = self.create_user(
            username=username,
            email=self.normalize_email(email),
            password=password,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user

class CustomUser(AbstractBaseUser):
    #중복방지 primary_key=True
    username = models.CharField(max_length=30, unique=True)
    email = models.EmailField(default='', max_length=100, null=False, blank=False, unique=True)
    #아래 두개는 필수 필드라고 합니다!
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = UserManager() #위에서 정의한 헬퍼 클래스 불러와서 

    USERNAME_FIELD = 'username'
    #필수로 작성해야하는 필드 명시
    REQUIRED_FIELDS = ['email']

    def __str__(self):
        return self.username

#admin페이지에서 오류 잡는 용도입니다
    @property
    def is_staff(self):
        return self.is_admin
    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True
    

class MyPage(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    profile_image = models.ImageField(upload_to='images/user', blank=True)  
    def __str__(self):
        return self.user.id