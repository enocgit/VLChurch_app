from django.shortcuts import render
from django.views.generic import ListView
from fellowships.models import Fellowship

# 

class FellowshipsList(ListView):
    model = Fellowship
    template_name = 'fellowships/fellowship.html'
    context_object_name = 'fellowships'