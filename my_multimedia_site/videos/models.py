from django.db import models

class Video(models.Model):
    title = models.CharField(max_length=200)
    # Remove 'upload_to' - CharField only needs max_length
    video_file = models.CharField(max_length=500) 
    description = models.TextField(blank=True, null=True)
    is_visible = models.BooleanField(default=True)

    def __str__(self):
        return self.title
