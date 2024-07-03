from django.db import models


# Create your models here.

class Poem(models.Model):
    word = models.CharField(max_length=50)
    poem = models.TextField(max_length = 1000)
    def __str__(self):
        return self.poem
    
class PoemPost(models.Model):
    poem = models.ForeignKey(Poem, on_delete =  models.CASCADE)
    post = models.TextField(max_length = 1000)
    

class PostComment(models.Model):
    post = models.ForeignKey(PoemPost, on_delete = models.CASCADE)
    comment = models.TextField(max_length = 500)