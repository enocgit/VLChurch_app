from django.shortcuts import render
from django.views.generic import ListView
from .models import SundayService

# 
class ServiceList(ListView):
    model = SundayService
    template_name = 'sunday_services/sunday_services_list.html'
    context_object_name = 'services'
