#linh
#linh@gmail.com
#123456
from django.contrib import admin
from .models import Post, Project
from ckeditor.widgets import CKEditorWidget
from django.db import models
#admin.site.register(Post, PostAdmin)
#admin.site.register(Post)
# Register your models here.

#@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'publish', 'status']
    list_filter = ['status', 'created', 'publish']
    search_fields = ['title', 'body']
    prepopulated_fields = {'slug': ('title',)}
    date_hierarchy = 'publish'
    ordering = ['status', 'publish']
    formfield_overrides = {
        models.TextField: {'widget': CKEditorWidget},
    }

admin.site.register(Post, PostAdmin)

class ProjectAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'publish', 'status']
    list_filter = ['status', 'created', 'publish']
    search_fields = ['title', 'body']
    prepopulated_fields = {'slug': ('title',)}
    date_hierarchy = 'publish'
    ordering = ['status', 'publish']
    formfield_overrides = {
        models.TextField: {'widget': CKEditorWidget},
    }

admin.site.register(Project, ProjectAdmin)