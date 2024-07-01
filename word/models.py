from django.contrib.auth.models import User
from django.db import models
from poem.models import PoemPost, PostComment


# Create your models here.

class Word(models.Model):
    word = models.CharField(max_length = 10)
    description = models.CharField(max_length = 500)
    example = models.CharField(max_length = 500)
class WordUser(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    word = models.ForeignKey(Word, on_delete=models.CASCADE)
    writeTime = models.DateTimeField(auto_now_add=True)
class Notice(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    post = models.ForeignKey(PoemPost, on_delete = models.CASCADE)
    postComment = models.ForeignKey(PostComment, on_delete = models.CASCADE)





