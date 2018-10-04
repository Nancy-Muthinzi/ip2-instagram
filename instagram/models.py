from django.db import models

class Profile(models.Model):
    profile_photo = models.ImageField(upload_to = 'home')
    bio = models.TextField(max_length = 144)

    def save_profile(self):
        self.save()

    def delete_profile(self):        
        self.delete()

    def __str__(self):
        return self.name

class Image(models.Model):
    image = models.ImageField(upload_to = 'home/')
    image_name = models.CharField(max_length = 50)
    image_caption = models.TextField(max_length = 144)
    # profile = models.ForeignKey(Profile)
    # likes = models.IntergerField(max_length = 25, blank=True)
    likes = models.CharField(max_length = 25, blank=True)
    comments = models.TextField(max_length = 144, blank=True)
    # pub_date = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return self.image_name

    class Meta:
        ordering = ['image_name']

    def save_image(self):
        self.save()

    def delete_image(self):
        self.delete()

    @classmethod
    def search_by_category(cls,search_term):
        gallery = cls.objects.filter(image_category__name__icontains=search_term)
        return images
    @classmethod
    def retrive_all_images(cls):
        images = Image.objects.all()
        return images

    @classmethod
    def get_image_by_id(cls, id):
        images = cls.objects.get(pk=id)
        return images  

class Comment(models.Model):
    name = models.CharField(max_length = 144)