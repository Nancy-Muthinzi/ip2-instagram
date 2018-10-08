from django.db import models
from django.contrib.auth.models import User
from tinymce.models import HTMLField

class Profile(models.Model):
    profile_photo = models.ImageField(upload_to='profile/')
    name = models.CharField(max_length= 25, default=True) 
    bio = models.TextField(max_length= 144, default=True) 
    user=models.OneToOneField(User,on_delete=models.CASCADE)

    def save_profile(self):
        self.save()

    def delete_profile(self):        
        self.delete()

    def __str__(self):
        return self.name     

class Image(models.Model):
    image = models.ImageField(upload_to = 'home/', blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image_name = models.CharField(max_length = 25, blank=True)
    image_caption = models.TextField(max_length = 144)
    profile = models.TextField(max_length=50, blank=True)
    comments = models.TextField(max_length = 144, blank=True)

    def __str__(self):
        return self.image_caption

    class Meta:
        ordering = ['image_caption']

    def save_image(self):
        self.save()

    def delete_image(self):
        self.delete()

    @classmethod
    def search_by_image_name(cls,search_term):
        instagram = cls.objects.filter(image_name__icontains=search_term)
        return instagram

    @classmethod
    def retrive_all_images(cls):
        images = Image.objects.all()
        return images

    @classmethod
    def get_image_by_id(cls, id):
        images = cls.objects.get(pk=id)
        return images  

class Comment(models.Model):
    user = models.ForeignKey(User, default=True, on_delete=models.CASCADE)
    comment = models.TextField(max_length = 144)
    image = models.ForeignKey(Image, on_delete=models.CASCADE, default= True)
    
class User(models.Model):
    name = models.CharField(max_length=25)
    username = models.CharField(max_length=25)
    email = models.EmailField()
    