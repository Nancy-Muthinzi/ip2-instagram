from django.contrib import admin
from .models import UserProfile,Image, Tag, Comment,Like

admin.site.register(UserProfile)
admin.site.register(Image)
admin.site.register(Tag)
admin.site.register(Comment)
admin.site.register(Like)