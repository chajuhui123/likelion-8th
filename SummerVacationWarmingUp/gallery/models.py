from django.db import models

class gallery_photo(models.Model):
    title = models.CharField(max_length=20)
    date = models.DateField(auto_now = False)
    photo = models.ImageField(upload_to = "media", blank = True)

