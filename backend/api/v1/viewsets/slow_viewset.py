
from django.http import JsonResponse
from rest_framework import viewsets

from data_processors.slow_processor import SlowDataRepository as data_repository


class SlowViewset(viewsets.ViewSet):
    """
    A simple ViewSet
    """
    def list(self, request):
        data_repo = data_repository()
        return JsonResponse({'data': data_repo.execute()})

    def create(self, request):
        pass

    def retrieve(self, request, pk=None):
        pass

    def update(self, request, pk=None):
        pass

    def partial_update(self, request, pk=None):
        pass

    def destroy(self, request, pk=None):
        pass