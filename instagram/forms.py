from django import forms
from .models import Comment 

class CommentForm(forms.Form):
    comment = forms.CharField(label = 'comment', max_length = 144)