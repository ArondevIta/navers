from rest_framework.decorators import action
from rest_framework.viewsets import ModelViewSet
from django.core import serializers
from projects.api.serializers import ProjectsSerializer
from projects.models import Projects
from rest_framework.response import Response
from django.http.response import HttpResponse
from navers.models import Navers
from navers.api.serializers import NaversSerializer


class ProjectsViewSet(ModelViewSet):

    def get_queryset(self):
        return Projects.objects.all()

    def list(self, request):
        name = self.request.query_params.get('name', None)
        projects = Projects.objects.all()

        if name:
            projects = Projects.objects.filter(name__icontains=name)

        data = serializers.serialize('json', projects)
        return HttpResponse(data, content_type='application/json')

    @action(methods=['get'], detail=True)
    def show(self, request, pk=None):
        try:
            projects = Projects.objects.get(pk=pk)
            navers = Navers.objects.filter(projects=pk).values('id', 'name', 'birthdate', 'admission_date', 'job_role')
            serializer = ProjectsSerializer(projects)
            return Response({
                'projects': serializer.data,
                'navers': navers
            })
        except:
            return Response({
                'error': 'Project does not exists'
            })

    def create(self, request):
        project = Projects()
        project.name = request.data.get('name')
        project.save()

        navers = request.data.get('navers')

        for naver in navers:
            try:
                nav = Navers.objects.get(pk=naver)
                nav.projects.add(project)
            except:
                return Response({'error'})
        return Response({
            'name': project.name,
            'navers': navers
        })

    def update(self, request, pk=None):
        try:
            project = Projects.objects.get(pk=pk)
            project.name = request.data.get('name')
            project.save()
        except:
            return Response({'error'})

        serializer = ProjectsSerializer(project)

        return Response({
            'name': serializer.data['name']
        })
