from django.contrib import admin
from .models import Profile,Image, Tag, Comment,Like

admin.site.register(Profile)
admin.site.register(Image)
admin.site.register(Tag)
admin.site.register(Comment)
admin.site.register(Like)