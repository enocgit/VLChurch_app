from django.urls import path
from .views import ServiceList, getRecapId

app_name = 'service'

urlpatterns = [
    path('', ServiceList.as_view(), name='service-list'),
    path('get-recap-id', getRecapId, name='get-recap-id')
]
