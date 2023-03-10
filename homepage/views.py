from django.shortcuts import render
from django.views.generic import ListView
from leaders.models import *
from chats.models import CarouselImg

# homepage
class HomePage(ListView):
    model = Leader
    template_name = 'homepage/index.html'
    context_object_name = 'leaders'
    
    def get_context_data(self):
        leaderModel = Leader.objects.all()
        carouselModel = CarouselImg.objects.all()
        context = super().get_context_data()
        context['leaders'] = leaderModel
        context['carouselImgs'] = carouselModel
        
        return context
        

def view_about_page(request):
    return render(request, 'about.html')

def view_contact_page(request):
    return render(request, 'contact.html')
    
    
    
# def view_homepage(request):
#     return render(request, 'homepage/index.html')
