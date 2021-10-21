from django.db import models

# Create your models here.
class Comments(models.Model):
    message =  models.CharField(max_length=280, blank = True, null = True, default = '')
    likes = models.IntegerField(default = 0, null = True, blank = True)
    dislikes = models.IntegerField(default = 0, null = True, blank = True)
    video = models.CharField(max_length=280, null = True)

class Replies(models.Model):
    comment = models.ForeignKey(Comments, on_delete=models.CASCADE, default = '')
    message = models.CharField(max_length=280, blank = True, null = True, default = '')