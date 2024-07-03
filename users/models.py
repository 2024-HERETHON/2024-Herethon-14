from django.db import models
from django.contrib.auth.models import AbstractUser # 장고의 기본 사용자 모델, 사용자 인증 시스템에 필요한 기본 필드 제공

class User(AbstractUser):
    email = models.EmailField(max_length = 30, unique = True, null = False, blank = False) # 이메일

    def __str__(self):
        return f'{self.username}'