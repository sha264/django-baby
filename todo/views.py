
from django.shortcuts import render
from django.urls import path
from django.http import HttpResponse
from .models import Todo, User, Tag
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.views import APIView

class TodoAddView(APIView):
    def post(self, request):
        user_id = request.data["author"]
        user = User.objects.get(id=user_id) 
        Todo.objects.create(
            title=request.data["title"],
            description=request.data["description"],
            author=user,
            completed=request.data["completed"],
            duedate=None,
        )
        return Response(status=201)

class TodoDeleteView(APIView):
    def delete(self, request, id):
        todo = Todo.objects.get(id=id)
        todo.delete()
        return Response(status=204)

def get_todos_from_tag(request, id):
    tag = Tag.objects.get(id=id)
    todos = tag.todos.all()
    return JsonResponse({
        "todos": [todo.title for todo in todos]
    })


def get_tags_from_todo(request, id):
    todo = Todo.objects.get(id=id)
    tags = todo.tags.all()
    return JsonResponse({
        "tags": [tag.name for tag in tags]
    })

def get_todo_including_user_name(request, id):
    todo = Todo.objects.get(id=id)
    return JsonResponse({
        "title": todo.title,
        "description": todo.description,
        "name": todo.author,
        "completed": todo.completed,
        "duedate": todo.duedate
    })


def get_todos_from_user(request, id):
    user = User.objects.get(id=id)
    todos = user.todos.all() #userに紐づいているTodoを取ってこれる！ (related_name='todos'と定義しているおかげ)
    return JsonResponse({
        "todos": [todo.title for todo in todos]
    })

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
