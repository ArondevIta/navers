from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from django.core import serializers
from projects.api.serializers import ProjectsSerializer
from projects.models import Projects
from rest_framework.response import Response
from django.http.response import HttpResponse
from navers.models import Navers
from navers.api.serializers import NaversSerializer


class ProjectsViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]

    def get_queryset(self):
        return Projects.objects.all()

    def list(self, request):
        try:
            projects = Projects.objects.filter(user=request.user)
            if projects:
                name = self.request.query_params.get('name', None)
                if name:
                    projects = Projects.objects.filter(name__icontains=name)
                data = serializers.serialize('json', projects)
                return HttpResponse(data, content_type='application/json')
            else:
                return Response({
                    'error': 'No projects registered for this user'
                })
        except:
            return Response({
                'error'
            })

    @action(methods=['get'], detail=True)
    def show(self, request, pk=None):
        try:
            project = Projects.objects.get(pk=pk)
            if project.user == request.user:
                navers = Navers.objects.filter(projects=pk).values(
                    'id',
                    'name',
                    'birthdate',
                    'admission_date',
                    'job_role'
                )
                serializer = ProjectsSerializer(project)
                return Response({
                    'project': serializer.data,
                    'navers': navers
                })
            else:
                return Response({
                   'error': 'Project not registered for this user'
                })
        except:
            return Response({
                'error': 'Project does not exists'
            })

    def create(self, request):
        project = Projects()
        project.name = request.data.get('name')
        project.user = request.user
        project.save()

        navers = request.data.get('navers')

        if navers:
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
        else:
            return Response({
                'name': project.name,
                'navers': ''
            })

    def update(self, request, pk=None):
        try:
            project = Projects.objects.get(pk=pk)
            if project.user == request.user:
                project.name = request.data.get('name')
                project.save()
                serializer = ProjectsSerializer(project)
                return Response({
                    'name': serializer.data['name']
                })
            else:
                return Response({
                    'error': 'Project not registered for this user'
                })
        except:
            return Response({'error'})

    def destroy(self, request, pk=None):
        try:
            project = Projects.objects.get(pk=pk)
            if project.user == request.user:
                project.delete()
                return Response({
                    ''
                })
            else:
                return Response({
                    'error': 'Project not registered for this user'
                })
        except:
            return Response({
                'error'
            })
