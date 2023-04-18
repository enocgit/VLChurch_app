from django.urls import path
from .views import ProgrammesList

app_name = 'programmes'

urlpatterns = [
    path('', ProgrammesList.as_view(), name='programmes-list'),
]
