from django.urls import path
from .views import FellowshipsList

app_name = 'fellowships'

urlpatterns = [
    path('', FellowshipsList.as_view(), name='fellowships-list')
]