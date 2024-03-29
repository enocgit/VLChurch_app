from django.db import models
from django.contrib.auth.models import AbstractUser
from django_fields import DefaultStaticImageField
# from fellowships.models import Fellowship


# members
class Member(AbstractUser):  # members inheriting from AbstractUser model
    # username = models.CharField(max_length=100, unique=True)
    # name = models.CharField(max_length=255, null=True, blank=True)
    # picture = models.ImageField(upload_to='images', height_field=None, width_field=None,
    #                             max_length=None, null=True, blank=True, default='static/images/no_image.png')
    picture = DefaultStaticImageField(upload_to='images', height_field=None, width_field=None, max_length=None, null=True, blank=True, default_image_path='images/no_image.png')
    birthday = models.DateField(null=True, blank=True)
    # fellowship = models.ForeignKey(Fellowship, null=True, blank=True, on_delete=models.SET_NULL)
    fellowship = models.ManyToManyField(
        'fellowships.Fellowship', verbose_name='fellowship group', blank=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
        # return self.username

    class Meta:
        ordering = ['first_name']
