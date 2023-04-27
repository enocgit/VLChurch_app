from django.db import models
from django_fields import DefaultStaticImageField
import os


# guests
class Guest(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=100, null=True, blank=True)
    guest_from = models.CharField(max_length=255, null=True, blank=True)
    # picture = models.ImageField(upload_to='images', height_field=None,
    #                             width_field=None, max_length=None, null=True, blank=True, default='static/images/no_image.png' )
    picture = DefaultStaticImageField(upload_to='images', height_field=None,
                                width_field=None, max_length=None, null=True, blank=True, default_image_path='images/no_image.png' )

    def __str__(self):
        return self.name
    
    class Meta:
       ordering = ['name']

# programmes


class Programme(models.Model):
    # image = DefaultStaticImageField('background image', upload_to='images', height_field=None, width_field=None,
    #                           max_length=None, null=True, blank=True, default_image_path='images/programme_default.jpg')
    image = models.ManyToManyField('ProgrammeBackgroundImgs', blank=True, verbose_name='Background image')
    name = models.CharField('programme', max_length=255)
    datetime = models.DateTimeField('date & time', auto_now=False)
    venue = models.CharField(max_length=255, null=True, blank=True,
                             default='Victorious Living Church International, Kasoa')
    guests = models.ManyToManyField('Guest', blank=True)

    def __str__(self):
        return self.name

    class Meta:
       ordering = ['datetime']


class ProgrammeBackgroundImgs(models.Model):
    image = models.ImageField('Programme Background Image')

    def __str__(self):
        # return self.image.url
        return os.path.basename(self.image.name)
    

    class Meta:
        verbose_name_plural = 'Programme Background Images'