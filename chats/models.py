from django.db import models
from members.models import Member
from django.contrib.auth import get_user_model


# winner
class Winner(models.Model):
    member = models.ForeignKey(Member, verbose_name='name', on_delete=models.CASCADE, null=True, blank=True)
    # wins = models.IntegerField()
    
    def __str__(self):
        return self.member.name
    
# quizzes
class Quiz(models.Model):
    question = models.TextField()
    answer = models.TextField(null=True, blank=True)
    question_by = models.ForeignKey(Member, verbose_name="Question by", on_delete=models.CASCADE, null=True)
    winner = models.ManyToManyField('Winner', verbose_name='select winner(s)', null=True, blank=True)
    display_winner = models.BooleanField('display winner', default=False)
    
    def __str__(self):
        return self.question


# carousel images
class CarouselImg(models.Model):
    image = models.ImageField(upload_to='static/uploads', height_field=None, width_field=None, max_length=None)

    def __str__(self):
        return f'{self.image}'
    
    
# chat
class Chat(models.Model):
    name = models.CharField(max_length=60 )
    datetime = models.DateField(auto_now=False, auto_now_add=False)
    
    def __str__(self):
        return self.name
    
# comment
class Comment(models.Model):
    message = models.TextField(default='')
    user = models.ForeignKey(get_user_model(), verbose_name='member', on_delete=models.CASCADE)
    datetime = models.DateTimeField(auto_now=False, auto_now_add=False)
    chat = models.ForeignKey('Chat', on_delete=models.CASCADE, null=True, blank=True)
    
    def __str__(self):
       return self.message