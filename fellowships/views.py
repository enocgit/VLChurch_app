from django.shortcuts import render
from django.views.generic import ListView
from fellowships.models import Fellowship
import datetime

# 

class FellowshipsList(ListView):
    model = Fellowship
    template_name = 'fellowships/fellowship.html'
    context_object_name = 'fellowships'

    def get_context_data(self, **kwargs):
           context = super().get_context_data(**kwargs)
           context['current_year'] = datetime.date.today().year
           return context