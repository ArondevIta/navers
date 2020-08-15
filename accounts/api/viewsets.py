from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from accounts.api.serializers import UserSerializer
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token


class UserViewSet(ModelViewSet):
    serializer_class = UserSerializer

    def get_queryset(self):
        return User.objects.all()

    def create(self, request, *args, **kwargs):
        username = request.data['email']
        email = request.data['email']
        password = request.data['password']
        try:
            newUser = User.objects.create_user(username=username, email=email, password=password)
            newUser.save()
            token = Token.objects.create(user=newUser)
            return Response({
                'success': 'Usúario criado com sucesso!',
            })
        except:
            return Response({
                'error': 'Erro ao criar usúario'
            })
