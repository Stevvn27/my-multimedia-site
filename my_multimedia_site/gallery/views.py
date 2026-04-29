from django.shortcuts import render
from django.http import HttpResponse

def  gallery_view(request):
    return HttpResponse("Gallery Home Page")
