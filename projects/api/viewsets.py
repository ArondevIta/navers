from rest_framework.viewsets import ModelViewSet
from projects.api.serializers import ProjectsSerializer
from projects.models import Projects


class ProjectsViewSet(ModelViewSet):
    queryset = Projects.objects.all()
    serializer_class = ProjectsSerializer
