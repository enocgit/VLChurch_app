from django.shortcuts import render
from django.views.generic import ListView, View
from leaders.models import *
from chats.models import CarouselImg
from django.utils import timezone
import datetime

# homepage
class HomePage(ListView):
    model = Leader
    template_name = 'homepage/index.html'
    context_object_name = 'leaders'
    # context_data = {'current_year': timezone.datetime.now().year}
    
    
    def get_context_data(self):
        leaderModel = Leader.objects.all().order_by('ref')
        context = super().get_context_data()
        context['leaders'] = leaderModel
        context['celebrated_members'] = check_birthday()
        context['current_year'] = datetime.date.today().year
        
        return context

    # def get(self, request, *args, **kwargs):
    #     context = self.get_context_data()
    #     return self.render_to_response(context)

# about page
def view_about_page(request):
    return render(request, 'about.html', context={'current_year': datetime.date.today().year})

# contact page
def view_contact_page(request):
    return render(request, 'contact.html', context={'current_year': datetime.date.today().year})



# Bithday display function
def check_birthday():
    members = Member.objects.all()
    today = datetime.date.today()
    celebrated_members = []

    for member in members:
        if member.birthday:
                birthday = member.birthday
                if (birthday.month == today.month) and ((birthday.day - today.day >= -2) and (birthday.day - today.day <= 2)):
                        #  print(f'{member.first_name} {member.last_name}  will be celebrated. {birthday}')
                            celebrated_members.append(member)

    return celebrated_members


class BirthdayCelebration(ListView):
    model = Member
    template_name = 'birthday.html'
    # context_object_name = 'celebrated_members'
    

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['celebrated_members'] = check_birthday()
        context['current_year'] = datetime.date.today().year

        return context

# print('TIME OUTSIDE:', datetime.date(1999, 7, 15))
