from django.shortcuts import render
from django.views.generic import ListView
from .models import SundayService

# 
class ServiceList(ListView):
    model = SundayService
    template_name = 'service/service_list.html'
    context_object_name = 'service'
