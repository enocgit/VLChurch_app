from django.db import models

from fellowships.models import MusicGroup

# from django.contrib.contenttypes.fields import GenericForeignKey
# from django.contrib.contenttypes.models import ContentType
from members.models import Member
from programmes.models import Guest
# from programmes.models import Guest


# sunday services
class SundayService(models.Model):
    # other fields...
    # teacher_content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE, null=True, blank=True)
    # teacher_object_id = models.PositiveIntegerField(null=True, blank=True)
    # teacher = GenericForeignKey('teacher_content_type', 'teacher_object_id')
    teacher = models.ForeignKey(Member, related_name='teacher', verbose_name=('teacher'), on_delete=models.SET_NULL, null=True, blank=True)
    teacher2 = models.ForeignKey(Guest, related_name='teacher', verbose_name=('teacher (guest)'), on_delete=models.SET_NULL, null=True, blank=True)
    preacher = models.ForeignKey(Member, related_name='preacher', verbose_name=('preacher'), on_delete=models.SET_NULL, null=True, blank=True)
    preacher2 = models.ForeignKey(Guest, related_name='preacher', verbose_name=('preacher (guest)'), on_delete=models.SET_NULL, null=True, blank=True)
    datetime = models.DateTimeField('date & time', auto_now=False, null=True, blank=True)
    music_group = models.ForeignKey(MusicGroup, null=True, blank=True, on_delete=models.SET_NULL)
    venue = models.CharField(max_length=255, default='Victorious Living Church International, Kasoa')
    guests = models.ManyToManyField('programmes.Guest', verbose_name='Invited Guests', null=True, blank=True)
    image = models.ImageField('background image', upload_to='static/uploads', height_field=None, width_field=None, max_length=None, null=True, blank=True, default='static/images/sunday_service_bg.jpg')
    
# class Service(models.Model):
#     teacher = models.CharField(max_length=255, null=True, blank=True)
#     preacher = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return f'{self.datetime.date()} Sunday Church Service'
