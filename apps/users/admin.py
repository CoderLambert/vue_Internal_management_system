from django.contrib import admin
from users.models import UserProfile,Role,Department
# Register your models here.

class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'username','email','date_joined')
    search_fields = ('username','date_joined')
    list_filter = ('username', 'date_joined',)


class RoleAdmin(admin.ModelAdmin):
    list_display = ('id','name')

class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('id','name')

admin.site.register(Role,RoleAdmin)
admin.site.register(Department,DepartmentAdmin)
admin.site.register(UserProfile,UserProfileAdmin)