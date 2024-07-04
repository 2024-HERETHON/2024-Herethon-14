from django.contrib.auth import get_user_model
from django.db import models
from poem.models import PoemPost, PostComment


# Create your models here.

class Word(models.Model):
    word = models.CharField(max_length = 10)
    description = models.CharField(max_length = 500)
    example = models.CharField(max_length = 500)
    def __str__(self):
        return self.word
    
class WordUser(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    word = models.ForeignKey(Word, on_delete=models.CASCADE)
    writeTime = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.word
    
class Notice(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete = models.CASCADE)
    post = models.ForeignKey(PoemPost, on_delete = models.CASCADE)
    postComment = models.ForeignKey(PostComment, on_delete = models.CASCADE)
    write_time=models.DateTimeField(auto_now_add=True)





