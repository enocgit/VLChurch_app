from django.shortcuts import render
from django.views.generic import ListView
from .models import Gallery

# Create your views here.
class ViewGallery(ListView):
    model = Gallery
    template_name = 'gallery/gallery.html'
    context_object_name = 'gallery'