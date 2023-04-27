from django.shortcuts import render
from django.views.generic import ListView
from .models import Programme
import datetime

# 
class ProgrammesList(ListView):
    model = Programme
    template_name = 'programmes/programmes_list.html'
    context_object_name = 'programmes'

    def get_context_data(self, **kwargs):
       context = super().get_context_data(**kwargs)
       context['current_year'] = datetime.date.today().year
       return context
