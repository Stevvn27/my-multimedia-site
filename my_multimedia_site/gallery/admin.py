from django.contrib import admin
from .models import MediaItem
class GalleryAdmin(admin.ModelAdmin):
    list_display = ['title', 'is_visible']
    actions = ['make_published', 'make_hidden']

    @admin.action(description='Publish selected items')
    def make_published(self, request, queryset):
        queryset.update(is_visible=True)

    @admin.action(description='Hide selected items')
    def make_hidden(self, request, queryset):
        queryset.update(is_visible=False)

admin.site.register(MediaItem, GalleryAdmin)

# Register your models here.
