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
from django.conf import settings
from django.contrib import admin
from django.urls import path,re_path,include
from django.conf.urls.static import static
from django.views.generic import TemplateView

from rest_framework import routers
from rest_framework_jwt.views import obtain_jwt_token
from rest_framework.documentation import include_docs_urls

from users.views import UserViewset, UserOptionViewset, RoleViewset, DepartmentViewset
from project.views import ProjecsListViewSet, ProjectNameListViewSet, RomImagesListViewSet, MachinesListViewSet
from support.views import WebSiteLinkListViewSet, WebSiteTypeListViewSet, ResourceTypeListViewSet, CloundResourceListViewSet, DemandListViewSet
from articals.views import ArticaleListViewSet,NoteListViewSet,ImageMetaListViewSet, ArticleTypeListViewSet #,MetaImageView
# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()

#配置 snippets
router.register(r'users', UserViewset, basename="users")
router.register(r'roles', RoleViewset, basename="roles")
router.register(r'departments', DepartmentViewset, basename="departments")
router.register(r'images', RomImagesListViewSet, basename="images")
router.register(r'projects', ProjecsListViewSet, basename="projects")
router.register(r'project/name', ProjectNameListViewSet, basename="project_name")
router.register(r'machines', MachinesListViewSet, basename="machines")
router.register(r'web/site', WebSiteLinkListViewSet, basename="web_site")
router.register(r'web/type', WebSiteTypeListViewSet, basename="web_type")
router.register(r'resource/clound', CloundResourceListViewSet, basename="resource_clound")
router.register(r'resource/type', ResourceTypeListViewSet, basename="resource_type")
router.register(r'suggest/demand', DemandListViewSet, basename="demand")
router.register(r'articles', ArticaleListViewSet, basename="articles")
router.register(r'notes', NoteListViewSet, basename="notes")
router.register(r'article/types',ArticleTypeListViewSet,basename="article_type")

router.register(r'meta/image',ImageMetaListViewSet,basename="meta_image")
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
proname_list = ProjectNameListViewSet.as_view({
    'get': 'list'
})

machine_list = MachinesListViewSet.as_view({
    'get': 'list'
})

website_list = WebSiteLinkListViewSet.as_view({
    'get': 'list'
})

webtype_list = WebSiteTypeListViewSet.as_view({
    'get': 'list'
})

demand_list = DemandListViewSet.as_view({
    'get': 'list'
})

articles_list = ArticaleListViewSet.as_view({
    'get':'list'
})

notes_list = NoteListViewSet.as_view({
    'get':'list'
})

meta_image_list = ImageMetaListViewSet.as_view({
    'get':'list'
})

articles_list = ArticaleListViewSet.as_view({
    'get':'list'
})
urlpatterns = [
    path('admin/', admin.site.urls),
    # path('api/delete/image/',MetaImageView.as_view(),name='delete_image'),
    path('api/', include(router.urls)),
    path('docs/', include_docs_urls(title="Beyond PLM")),

    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('api/login', obtain_jwt_token),
    path('', TemplateView.as_view(template_name="index.html"), name='index'),
    # re_path(r'.*', TemplateView.as_view(template_name='index.html'), name='index')
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

