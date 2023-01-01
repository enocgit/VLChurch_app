from django.shortcuts import render
from django.views.generic import ListView
from fellowships.models import Fellowship

# 

class FellowshipsList(ListView):
    model = Fellowship
    template_name = 'fellowship_list.html'
    context_object_name = 'fellowships'
