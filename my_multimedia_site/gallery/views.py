from django.shortcuts import render
from django.http import HttpResponse

def  gallery_view(request):
     return render(request, 'gallery/gallery.html')
