from django.forms import models
from django import forms
from .models import Comment
from ckeditor.fields import RichTextField


class CommentForm(models.ModelForm):
    
    class Meta:
        model = Comment
        fields = ['message']
        labels = {
            'message': ''
        }
        # widgets = {
        #     'message': forms.Textarea(attrs={
        #         'class': 'form-control rounded-4 p-3',
        #         'cols': '40', 'rows': '10',
        #         # 'id': 'comment-field',
        #      })
        # }