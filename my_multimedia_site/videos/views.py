from django.shortcuts import render
from .models import Video

def video_list(request):
    videos = Video.objects.all()
    videos = Video.objects.filter(is_visible=True) 
    return render(request, 'videos/video_list.html', {'videos': videos})

# Create your views here.
