from django.contrib import admin
from .models import Profile, Image, Comment, User

admin.site.register(Profile)
admin.site.register(Image)
admin.site.register(Comment)
admin.site.register(User)
