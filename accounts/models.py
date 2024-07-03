from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model

class Profile(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete = models.CASCADE)
    userImage = models.ImageField(default='img/alarmImg.svg', upload_to="%Y/%m/%d")

    def __str__(self):
        return self.user.username