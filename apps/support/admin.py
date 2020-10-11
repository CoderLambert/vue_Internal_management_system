from django.contrib import admin
from support.models import ResourceType, CloundResource, WebSiteType, WebSiteLink, Demand
# Register your models here.
from mptt.admin import MPTTModelAdmin, DraggableMPTTAdmin
from support.models import Genre
from django.utils.html import format_html

class GenreMPTTModelAdmin(DraggableMPTTAdmin):
    # specify pixel amount for this ModelAdmin only:
    mptt_level_indent = 20

    # def something(self, instance):
    #     return format_html(
    #         '<div style="text-indent:{}px">{}</div>',
    #         instance._mpttfield('level') * self.mptt_level_indent *2,
    #         instance.name,  # Or whatever you want to put here
    #     )
    # something.short_description = _('something nice')

class ResourceTypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name','add_time')
    search_fields = ('name','add_time')
    list_filter = ('name', 'add_time',)


class CloundResourceAdmin(admin.ModelAdmin):
    list_display = ('id','name', 'url', 'type', 'description',)
    search_fields = ('id', 'url', 'type', 'add_time')
    list_filter = ('type',
                   'add_time',)


class WebSiteTypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name','add_time')
    search_fields = ('name','add_time')
    list_filter = ('name', 'add_time',)


class WebSiteLinkAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'url', 'type', 'description',)
    search_fields = ('id', 'url', 'type', 'add_time')
    list_filter = ('type',
                   'add_time',)


class DemandAdmin(admin.ModelAdmin):
    list_display = ('id', 'description', 'current_state', 'owner')
    search_fields = ('id', 'description', 'current_state', 'owner')
    list_filter = ('current_state',
                   'owner',)


admin.site.register(ResourceType, ResourceTypeAdmin)
admin.site.register(CloundResource, CloundResourceAdmin)
admin.site.register(WebSiteType, WebSiteTypeAdmin)
admin.site.register(WebSiteLink, WebSiteLinkAdmin)
admin.site.register(Genre, GenreMPTTModelAdmin)
admin.site.register(Demand, DemandAdmin)
