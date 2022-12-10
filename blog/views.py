from django.shortcuts import render
from django.urls import path
from django.http import HttpResponse
from .models import Blog
from django.http import JsonResponse


# Create your views here.
def blog_list(request):
    tasks = Blog.objects.all()
    data = {
        "blogs":list(tasks.values())
    }
    return JsonResponse(data)

def blog_get(request, id):
    item = Blog.objects.filter(id=id)
    data = {
        "item":list(item.values())
    }
    return JsonResponse(data)

def blog_like(request):
    return HttpResponse("いいねしました！")