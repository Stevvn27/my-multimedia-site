from django.contrib import admin
from .models import Video

# This class controls how Video looks and behaves in the admin panel
class VideoAdmin(admin.ModelAdmin):
    list_display = ['title', 'is_visible'] # Adds a status column
    actions = ['make_published', 'make_hidden'] # Adds the bulk menu

    @admin.action(description='Publish selected videos')
    def make_published(self, request, queryset):
        queryset.update(is_visible=True)

    @admin.action(description='Hide selected videos')
    def make_hidden(self, request, queryset):
        queryset.update(is_visible=False)

# Register the model with the new VideoAdmin settings
admin.site.register(Video, VideoAdmin)

# Register your models here.
