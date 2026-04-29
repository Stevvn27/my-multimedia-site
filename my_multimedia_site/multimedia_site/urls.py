from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('gallery.urls')),
     path('videos/', include('videos.urls')), 
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

from django.contrib.auth.models import User
from django.http import HttpResponse

def create_admin(request):
    if not User.objects.filter(username='admin').exists():
        User.objects.create_superuser('admin', 'admin@example.com', 'password123')
        return HttpResponse("Admin account 'admin' created with password 'password123'")
    return HttpResponse("Admin already exists.")

# Add this to your urlpatterns list:
urlpatterns += [path('makeadmin/', create_admin)]
