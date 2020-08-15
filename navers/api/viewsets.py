from django.core import serializers
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from django.http.response import HttpResponse, JsonResponse
from navers.api.serializers import NaversSerializer
from navers.models import Navers


class NaversViewSet(ModelViewSet):
    serializer_class = NaversSerializer

    def get_queryset(self):
        return Navers.objects.all()

    def list(self, request, *args, **kwargs):
        navers = Navers.objects.all()
        data = serializers.serialize('json', navers)
        return HttpResponse(data, content_type='application/json')

    @action(methods=['get'], detail=True)
    def show(self, request, pk=None):
        try:
            navers = Navers.objects.get(pk=pk)
            serializer = NaversSerializer(navers)
            return Response(serializer.data)
        except:
            return Response({
                'error': 'Naver does not exists'
            })
