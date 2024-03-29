from django.db import models


# fellowships
class Fellowship(models.Model):
    name = models.CharField('fellowship', max_length=255)
    # meeting_days = models.CharField(max_length=100, null=True, blank=True)
    meeting_days = models.ManyToManyField('MeetingDay', blank=True)

    def __str__(self):
        return self.name

    class Meta:
       ordering = ['name']
# music_group


class MusicGroup(models.Model):
    name = models.CharField('music group', max_length=50)

    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['name']


# Meeting days
class MeetingDay(models.Model):
    name = models.CharField('day', max_length=15, null=False, blank=False)

    class Meta:
        ordering = ['id']

    def __str__(self):
        return self.name