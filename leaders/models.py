from django.db import models
from members.models import Member


# Leader_titles
class LeaderTitle(models.Model):
    name = models.CharField('title', max_length=255)
    
    def __str__(self):
        return self.name
    
    class Meta:
       ordering = ['name']
    
# leaders
class Leader(models.Model):
    # member = models.ForeignKey(Member, verbose_name='name', null=True, blank=True, on_delete=models.CASCADE)
    member = models.OneToOneField(Member, verbose_name='name', null=True, blank=True, on_delete=models.CASCADE)
    # picture = models.ImageField(upload_to='static/uploaded_images', height_field=None, width_field=None, max_length=None, null=True, blank=True)
    title = models.ForeignKey(LeaderTitle, null=True, blank=True, on_delete=models.SET_NULL)
    position = models.CharField(max_length=50, null=True, blank=True)
    # birthday = models.DateField(auto_now=False, auto_now_add=False, null=True, blank=True)
    ref = models.CharField(max_length=1, default='D', null=False, blank=False)

    def __str__(self):
        return f'{self.member.first_name} {self.member.last_name}'
    
    class Meta:
        ordering = ['member']
