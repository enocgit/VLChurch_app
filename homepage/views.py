from django.shortcuts import render
from django.views.generic import ListView, View
from leaders.models import *
from chats.models import CarouselImg
from django.utils import timezone

# homepage
class HomePage(ListView):
    model = Leader
    template_name = 'homepage/index.html'
    context_object_name = 'leaders'
    # context_data = {'current_year': timezone.datetime.now().year}
    
    
    def get_context_data(self):
        leaderModel = Leader.objects.all().order_by('id')
        carouselModel = CarouselImg.objects.all()
        context = super().get_context_data()
        context['leaders'] = leaderModel
        context['carouselImgs'] = carouselModel
        context['current_year'] = timezone.datetime.now().year
        
        return context

    # def get(self, request, *args, **kwargs):
    #     context = self.get_context_data()
    #     return self.render_to_response(context)

def view_about_page(request):
    return render(request, 'about.html')

def view_contact_page(request):
    return render(request, 'contact.html')

    
    
# def view_homepage(request):
#     return render(request, 'homepage/index.html')
