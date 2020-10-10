# model Form 이용해서 하는 법

from django.db import models

class FirstModel(models.Model):
    x = (
        ('GOOD','좋아요'),
        ('BAD', '싫어요'),
    )
    title = models.CharField(max_length=50)
    text = models.TextField()
    recommend = models.CharField(max_length = 5, choices = x)
    