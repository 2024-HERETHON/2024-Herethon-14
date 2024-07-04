from django.db import models
from django.contrib.auth.models import AbstractUser # 장고의 기본 사용자 모델, 사용자 인증 시스템에 필요한 기본 필드 제공
import os
from uuid import uuid4
from django.utils import timezone
from django.conf import settings

def upload_filepath(instance, filename):
        today_str = timezone.now().strftime("%Y%m%d")
        file_basename = os.path.basename(filename)
        return f'{instance._meta.model_name}/{today_str}/{str(uuid4())}_{file_basename}'

class User(AbstractUser):
    email = models.EmailField(max_length = 30, unique = True, null = False, blank = False) # 이메일
    userImage = models.ImageField(upload_to=upload_filepath) # 프로필 사진

    def __str__(self):
        return f'{self.username}'