from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from accounts.api.viewsets import UserViewSet
from rest_framework.authtoken.views import obtain_auth_token
from projects.api.viewsets import ProjectsViewSet
from navers.api.viewsets import NaversViewSet


router = routers.DefaultRouter()
router.register('accounts', UserViewSet, basename='accounts')
router.register('navers', NaversViewSet, basename='navers')
router.register('projects', ProjectsViewSet, basename='projects')

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('login/', obtain_auth_token),
]
