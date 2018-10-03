from django.db import models

# Create your models here.
class Image(models.Model):
    image = models.ImageField(upload_to = 'home')
    image_name = models.CharField(max_length = 50)
    image_caption = models.TextField(max_length = 50)
    # profile = models.ForeignKey(Profile)
    likes = models.CharField(max_length = 25)
    comments = models.TextField(max_length = 144)
