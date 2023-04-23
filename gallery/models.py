from django.db import models

class Gallery(models.Model):
    picture = models.ImageField(upload_to='images')
