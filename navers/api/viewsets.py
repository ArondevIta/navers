from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from navers.api.serializers import NaversSerializer
from navers.models import Navers
from rest_framework.permissions import IsAuthenticated


class NaversViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]

    def get_queryset(self):
        return Navers.objects.all()

    @action(methods=['get'], detail=False)
    def index(self, request):
        try:
            naver = Navers.objects.filter(user=request.user)
            if naver:

                name = self.request.query_params.get('name', None)
                admission_date = self.request.query_params.get('admission_date', None)
                job_role = self.request.query_params.get('job_role', None)
                navers = Navers.objects.all().values('id', 'name', 'birthdate', 'admission_date', 'job_role')

                if name:
                    navers = Navers.objects.filter(name__iexact=name)

                if admission_date:
                    navers = Navers.objects.filter(admission_date__iexact=admission_date)

                if job_role:
                    navers = Navers.objects.filter(job_role__icontains=job_role)

                return Response(navers)
            else:
                return Response({
                    'error': 'No naver registered for this user'
                })
        except:
            return Response({
                'error'
            })

    @action(methods=['get'], detail=True)
    def show(self, request, pk=None):
        try:
            naver = Navers.objects.filter(user=request.user)
            if naver:
                try:
                    navers = Navers.objects.get(pk=pk)
                    serializer = NaversSerializer(navers)
                    return Response(serializer.data)
                except:
                    return Response({
                        'error': 'Naver does not exists'
                    })
            else:
                return Response({
                    'error': 'This naver noi registered for this user'
                })
        except:
            return Response({
                'error'
            })

    def create(self, request):
        naver = Navers()
        naver.name = request.data['name']
        naver.birthdate = request.data['birthdate']
        naver.admission_date = request.data['admission_date']
        naver.job_role = request.data['job_role']
        naver.user = request.user
        naver.save()
        projects = request.data.get('projects', None)

        if projects:
            for project in projects:
                naver.projects.add(project)

        serializer = NaversSerializer(naver)
        return Response(serializer.data)

    def update(self, request, pk=None):
        try:
            navers = Navers.objects.get(pk=pk)
            if navers.user == request.user:
                navers.name = request.data.get('name')
                navers.birthdate = request.data.get('birthdate')
                navers.admission_date = request.data.get('admission_date')
                navers.job_role = request.data.get('job_role')
                navers.save()

                serializer = NaversSerializer(navers)
                return Response(serializer.data)
            else:
                return Response({
                    'error': 'This nave not registered for this user'
                })
        except:
            return Response({'error'})

    def destroy(self, request, pk=None):
        try:
            naver = Navers.objects.get(pk=pk)
            if naver.user == request.user:
                print(naver)
                return Response('')
            else:
                return Response({
                    'error': 'This nave not registered for this user'
                })
        except:
            return Response({
                'error'
            })
