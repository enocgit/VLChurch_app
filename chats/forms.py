from django.forms import models
from django import forms
from .models import Comment
from ckeditor.fields import RichTextField


class CommentForm(models.ModelForm):

    # message = forms.CharField(widget=forms.Textarea(attrs={'class': 'focus:border-[#3e535f] focus:ring-[#3e535f]',}))
    
    class Meta:
        model = Comment
        fields = ['message']
        labels = {
            'message': ''
        }