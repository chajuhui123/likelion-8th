from django.db import models

# Create your models here.

class mlonList(models.Model):
    songName = models.CharField(max_length=100)
    singerName = models.CharField(max_length=100)
    rankNumber = models.IntegerField(default=0)
    imgScr = models.TextField(blank=True)