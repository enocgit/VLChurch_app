from django.shortcuts import render
from django.views.generic import ListView
from .models import Programme

# 
class ProgrammesList(ListView):
    model = Programme
    template_name = 'programmes/programmes_list.html'
    context_object_name = 'programmes'

