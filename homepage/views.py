from django.shortcuts import render
from django.views.generic import ListView
from leaders.models import *

# homepage
class HomePage(ListView):
    model = Leader
    template_name = 'homepage/index.html'
    context_object_name = 'leaders'

# def view_homepage(request):
#     return render(request, 'homepage/index.html')
