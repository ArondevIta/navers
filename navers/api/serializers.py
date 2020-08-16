from rest_framework import serializers
from navers.models import Navers
from projects.api.serializers import ProjectsSerializer


class NaversSerializer(serializers.ModelSerializer):

    projects = ProjectsSerializer(many=True, read_only=True)

    class Meta:
        model = Navers
        fields = ('id', 'name', 'birthdate', 'admission_date', 'job_role', 'projects')
