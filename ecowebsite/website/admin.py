from django.contrib import admin
from . import models




admin.site.register(models.Tag)


class AuthorAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug')

class ImageAdmin(admin.StackedInline):
    model = models.Image
 
class FileAdmin(admin.StackedInline):
    model = models.File
 
@admin.register(models.ProjectPost)
class PostAdmin(admin.ModelAdmin):
    inlines = [ImageAdmin, FileAdmin]
    list_display = ['title', 'date_created',]
 
    class Meta:
       model = models.ProjectPost
 
admin.site.register(models.Person)
admin.site.register(models.AboutCompanyText)


@admin.register(models.NewsPost)
class NewsPost(admin.ModelAdmin):
    inlines = [ImageAdmin, FileAdmin]
    list_display = ['title', 'date_created',]
 
    class Meta:
       model = models.NewsPost


class GalleryItemAdmin(admin.ModelAdmin):
    pass
admin.site.register(models.GalleryItem, GalleryItemAdmin)
