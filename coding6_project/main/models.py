from django.db import models

# Create your models here.

class myFriend(models.Model):
    image = models.ImageField(upload_to = "image", blank = True)
    title = models.CharField(max_length=30)
    text = models.TextField()

    recipe = models.TextField()