from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.generic import ListView
from .models import *

#


class ServiceList(ListView):
    model = SundayService
    template_name = 'service/service_list.html'
    # context_object_name = 'service'

    # def get_queryset(self, *args):
    #     service = SundayService.objects.last()
    #     return service
    # super().get_queryset(*args)

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        service = SundayService.objects.last()
        recap = SundayRecap.objects.last()
        context['service'] = service
        context['recap'] = recap
        return context

    # def get_context_data(self, *args):
    #     service = SundayService.objects.last()
    #     return service


def getRecapId(request):
    if request.method == 'GET':
        recap_id = request.GET.get('recap_id')
        recap_id = int(recap_id)
        print('RECAP_ID:', recap_id)
        sunday_recap = SundayRecap.objects.get(pk=recap_id)
        sunday_recap.views += 1
        sunday_recap.save()
        return HttpResponse('success')
