"""Basilisk URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from django.views.generic import TemplateView

from rest_framework.documentation import include_docs_urls

from rest_framework import routers, serializers, viewsets
from rest_framework_jwt.views import obtain_jwt_token

from users.views import UserViewset,UserOptionViewset,RoleViewset,DepartmentViewset

from project.views import ProjecsListViewSet,ProjecNameListViewSet,RomImagesListViewSet, \
     MachinesListViewSet

from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()

#配置 snippets
router.register(r'users', UserViewset, basename="users")
router.register(r'roles', RoleViewset, basename="roles")
router.register(r'departments', DepartmentViewset, basename="departments")
router.register(r'images', RomImagesListViewSet, basename="images")
router.register(r'projects', ProjecsListViewSet, basename="projects")
router.register(r'project/name', ProjecNameListViewSet, basename="project_name")
router.register(r'machines', MachinesListViewSet, basename="machines")

users_list = UserViewset.as_view({
    'get': 'list',
})

roles_list = RoleViewset.as_view({
    'get': 'list',
})

departments_list = DepartmentViewset.as_view({
    'get': 'list',
})

image_list = RomImagesListViewSet.as_view({
    'get':'list'
})

project_list = ProjecsListViewSet.as_view({
    'get': 'list'
})
proname_list = ProjecNameListViewSet.as_view({
    'get': 'list'
})

machine_list = MachinesListViewSet.as_view({
    'get': 'list'
})

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name="index.html"), name='index'),

    path('api/', include(router.urls)),
    path('docs/', include_docs_urls(title="Beyond PLM")),

    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('api/login', obtain_jwt_token),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
