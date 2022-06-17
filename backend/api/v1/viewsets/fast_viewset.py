
from django.http import JsonResponse, StreamingHttpResponse
from rest_framework import viewsets

from data_processors.fast_processor import FastDataRepository as data_repository


class FastViewset(viewsets.ViewSet):
    """
    A simple ViewSet
    """
    def list(self, request):
        print('fast_list')
        data_repo = data_repository()
        return StreamingHttpResponse(streaming_content=data_repo.execute())

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