from django.db import models

class Gallery(models.Model):
    picture = models.ImageField(upload_to='images')

    class Meta:
        verbose_name_plural = 'Galleries'
