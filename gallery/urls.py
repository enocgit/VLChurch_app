from django.urls import path
from .views import *


app_name = 'gallery'

urlpatterns = [
    path('', ViewGallery.as_view(), name='view-gallery')
]
