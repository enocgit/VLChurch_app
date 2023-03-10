from django.db import models


# guests
class Guest(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255, null=True, blank=True)
    guest_from = models.CharField(max_length=255, null=True, blank=True)
    picture = models.ImageField(upload_to='static/uploads', height_field=None, width_field=None, max_length=None, default='static/images/no_image.jpeg')
    
    def __str__(self):
        return self.name

# programmes
class Programme(models.Model):
    image = models.ImageField('background image', upload_to='static/uploads', height_field=None, width_field=None, max_length=None, null=True, blank=True, default='static/images/programme_default.jpg')
    name = models.CharField('programme', max_length=255)
    datetime = models.DateTimeField('date & time', auto_now=False)
    venue = models.CharField(max_length=255, null=True, blank=True, default='Victorious Living Church International, Kasoa')
    guests = models.ManyToManyField('Guest', null=True, blank=True)
    
    def __str__(self):
        return self.name