from django.db import models

class MediaItem(models.Model):
    title = models.CharField(max_length=100)
    image_file = models.CharField(max_length=500, blank=True, null=True)
    video_file = models.FileField(upload_to='videos/', blank=True, null=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    is_visible = models.BooleanField(default=True) 

    def __str__(self):
        return self.title
