from django import forms
from .models import Comment
from django.core.files.images import get_image_dimensions

class CommentForm(forms.ModelForm):
    comment = forms.CharField(label = 'comment', max_length = 144)
    class Meta:
        model = Comment
        fields = ('user','comment')
