
from django.shortcuts import render
from django.urls import path
from django.http import HttpResponse
from .models import Todo
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.views import APIView



class TodoAddView(APIView):
    def post(self, request):
        Todo.objects.create(
            title=request.data["title"],
            description=request.data["description"],
            completed=request.data["completed"],
            duedate=None,
        )
        return Response(status=201)

class TodoDeleteView(APIView):
    def delete(self, request, id):
        todo = todo.objects.get(id=id)
        todo.delete()
        return Response(status=204)

# Create your views here.
def todo_list(request):
    tasks = Todo.objects.all()
    data = {
        "tasks":list(tasks.values())
    }
    return JsonResponse(data)

def todo_add(request):
    return HttpResponse("")

def todo_delete(request):
    return HttpResponse("")

def todo_init(request):
    return HttpResponse("初期画面です")
