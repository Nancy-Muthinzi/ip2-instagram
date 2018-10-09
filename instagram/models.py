from django.db import models
from django.contrib.auth.models import User
from tinymce.models import HTMLField


class Profile(models.Model):
    profile_photo = models.ImageField(upload_to='profile/')
    name = models.CharField(max_length=25, default="Nancy K. Muthinzi")
    bio = models.TextField(max_length=144, default=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def save_profile(self):
        self.save()

    def delete_profile(self):
        self.delete()

    @classmethod
    def get_profiles(cls):
        profile = cls.objects.all()
        return profile

    @classmethod
    def search_by_username(cls, search_term):
        profile = cls.objects.filter(title__icontains=search_term)
        return profile

    def __str__(self):
        return self.name


class Image(models.Model):
    user = models.ForeignKey(User,related_name='images' ,on_delete=models.CASCADE)
    image = models.ImageField(upload_to='home/', blank=True)
    image_name = models.CharField(max_length=25, blank=True)
    image_caption = models.TextField(max_length=144)

    def __str__(self):
        return self.image_caption

    class Meta:
        ordering = ['image_caption']

    def save_image(self):
        self.save()

    def delete_image(self):
        self.delete()

    @classmethod
    def search_by_image_name(cls, search_term):
        instagram = cls.objects.filter(image_name__icontains=search_term)
        return instagram

    @classmethod
    def retrive_all_images(cls):
        images = Image.objects.all()
        return images

    @classmethod
    def get_images(cls):
        images = cls.objects.all()
        return images

    @classmethod
    def get_image_by_id(cls, id):
        images = cls.objects.get(pk=id)
        return images


class Comment(models.Model):
    user = models.ForeignKey(User, default=True, on_delete=models.CASCADE)
    comment = models.TextField(max_length=144)
    image = models.ForeignKey(Image, on_delete=models.CASCADE, default=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def save_comment(self):
        self.save()

    def delete_comment(self):
        self.delete()


class User(models.Model):
    name = models.CharField(max_length=25)
    username = models.CharField(max_length=25)
    email = models.EmailField()
    
