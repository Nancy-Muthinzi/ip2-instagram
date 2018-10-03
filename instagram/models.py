from django.db import models

class Profile(models.Model):
    profile_photo = models.ImageField(upload_to = 'home')
    bio = models.TextField(max_length = 144)


class Image(models.Model):
    image = models.ImageField(upload_to = 'home')
    image_name = models.CharField(max_length = 50)
    image_caption = models.TextField(max_length = 50)
    # profile = models.ForeignKey(Profile)
    likes = models.CharField(max_length = 25)
    comments = models.TextField(max_length = 144)
    pub_date = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return self.image_name

    class Meta:
        ordering = ['image_name']

    def save_image(self):
        self.save()

    def delete_image(self):
        self.delete()  

    # @classmethod
    # def update_caption(cls,update):
    #     instagram = cls.objects.filter
    #     (image_caption__name__icontains = update)
    #     return instagram
