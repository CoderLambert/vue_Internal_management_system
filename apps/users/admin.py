from django.contrib import admin
from users.models import UserProfile,Role
# Register your models here.

class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'username','email','date_joined')
    search_fields = ('username','date_joined')
    list_filter = ('username', 'date_joined',)


class RoleAdmin(admin.ModelAdmin):
    list_display = ('id',)
    # search_fields = ('username','date_joined')
    # list_filter = ('username', 'date_joined' ,)

admin.site.register(Role,RoleAdmin)
admin.site.register(UserProfile,UserProfileAdmin)