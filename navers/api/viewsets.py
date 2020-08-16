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
        name = self.request.query_params.get('name', None)
        admission_date = self.request.query_params.get('admission_date', None)
        job_role = self.request.query_params.get('job_role', None)
        navers = Navers.objects.all().values('id', 'name', 'birthdate', 'admission_date', 'job_role')

        print(navers)

        if name:
            navers = Navers.objects.filter(name__iexact=name)

        if admission_date:
            navers = Navers.objects.filter(admission_date__iexact=admission_date)

        if job_role:
            navers = Navers.objects.filter(job_role__icontains=job_role)

        return Response(navers)

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

    def create(self, request):
        naver = Navers()
        naver.name = request.data['name']
        naver.birthdate = request.data['birthdate']
        naver.admission_date = request.data['admission_date']
        naver.job_role = request.data['job_role']
        naver.save()
        projects = request.data['projects']

        for project in projects:
            naver.projects.add(project)

        serializer = NaversSerializer(naver)
        return Response(serializer.data)

    def update(self, request, pk=None):
        try:
            navers = Navers.objects.get(pk=pk)
            navers.name = request.data.get('name')
            navers.birthdate = request.data.get('birthdate')
            navers.admission_date = request.data.get('admission_date')
            navers.job_role = request.data.get('job_role')
            navers.save()

            serializer = NaversSerializer(navers)
            return Response(serializer.data)

        except:
            return Response({'error'})
