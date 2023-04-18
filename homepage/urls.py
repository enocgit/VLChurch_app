from django.urls import path
from django.http import HttpResponse
from homepage.views import *
# from leaders.views import *

app_name = 'homepage'

urlpatterns = [
    # path('', view_homepage, name='homepage'),
    path('', HomePage.as_view(), name='homepage'),
    path('about/', view_about_page, name='about'),
    path('contact/', view_contact_page, name='contact'),
]

