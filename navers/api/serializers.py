from rest_framework import serializers
from navers.models import Navers


class NaversSerializer(serializers.ModelSerializer):

    class Meta:
        model = Navers
        fields = '__all__'
