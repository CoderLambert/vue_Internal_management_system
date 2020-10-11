from django.contrib import admin
from articals.models import Articale, Note, ImageMeta, ArticleType

class ArticaleAdmin(admin.ModelAdmin):
    list_display = ('id', 'note','title', 'original','public','add_time','modified_time')
    search_fields = ('title', 'text_content')


class NoteAdmin(admin.ModelAdmin):
    list_display = ('id', 'name',)
    search_fields = ('name',)

class ImageMetaAdmin(admin.ModelAdmin):
    list_display = ('id', 'image','add_time')
    search_fields = ('id','image',)

class ArticleTypeAdmin(admin.ModelAdmin):
    list_display = ('id','name','parent_id')

admin.site.register(Articale, ArticaleAdmin)
admin.site.register(Note, NoteAdmin)
admin.site.register(ImageMeta, ImageMetaAdmin)
admin.site.register(ArticleType, ArticleTypeAdmin)
