from django.contrib import admin
from project.models import Project, RomImageFile, MachineInfo


# Register your models here.

class ProjectAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'add_time')
    search_fields = ('name', 'add_time')
    list_filter = ('name', 'add_time',)


class RomImageFileAdmin(admin.ModelAdmin):
    list_display = ('id', 'add_time', 'url', 'project')
    search_fields = ('id', 'add_time', 'url', 'project')
    list_filter = ('project',
                   'is_delete',
                   'add_time',)


class MachineInfoAdmin(admin.ModelAdmin):
    list_display = ('id', 'project')
    search_fields = ('id', 'project')
    list_filter = ('project',)


admin.site.register(RomImageFile, RomImageFileAdmin)
admin.site.register(Project, ProjectAdmin)
admin.site.register(MachineInfo, MachineInfoAdmin)
