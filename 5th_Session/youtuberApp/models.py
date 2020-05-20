from django.db import models

class Youtuber(models.Model):
    channel = models.CharField(max_length=30)
    creater = models.CharField(max_length=30)
    favDegree = models.IntegerField()
    onAir = models.BooleanField()
    subscriber = models.IntegerField()
    link1 = models.TextField()
    link2 = models.TextField()
    link3 = models.TextField()
