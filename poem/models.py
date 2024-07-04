from django.db import models
from django.contrib.auth import get_user_model


# Create your models here.

class Poem(models.Model):
    word = models.CharField(max_length=50)
    poem = models.TextField(max_length = 1000)
    def __str__(self):
        return self.poem
    
class PoemPost(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete = models.CASCADE)
    poem = models.ForeignKey(Poem, on_delete =  models.CASCADE)
    post = models.TextField(max_length = 1000)
    write_time=models.DateTimeField(auto_now_add=True)
    

class PostComment(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete = models.CASCADE)
    post = models.ForeignKey(PoemPost, on_delete = models.CASCADE)
    comment = models.TextField(max_length = 500)
    write_time=models.DateTimeField(auto_now_add=True)