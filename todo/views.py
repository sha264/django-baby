from django.shortcuts import render, redirect
from .models import Todo, User
from django.http import JsonResponse
from rest_framework.response import Response
from django.http import HttpResponse
from rest_framework.views import APIView

# Create your views here.


def test(request):
    return HttpResponse("hello world")


class TodoAddView(APIView):
    def post(self, request):
        user_id = request.data["author"]
        user = User.objects.get(id=user_id)
        Todo.objects.create(
            title=request.data["title"],
            memo=request.data["memo"],
            author=user,
            priority=request.data["priority"],
        )
        return Response(status=201)


class TodoDeleteView(APIView):
    def delete(self, request, id):
        todo = Todo.objects.get(id=id)
        todo.delete()
        return Response(status=204)


class TodoListView(APIView):
    def get(self, request, id):
        user = User.objects.get(id=id)
        todos = user.todos.all()
        return JsonResponse({
            "todos": [
                {
                    "id": todo.id,
                    "title": todo.title,
                    "memo": todo.memo,
                    "priority": todo.priority,
                    "author": todo.author.name,
                } for todo in todos
            ]
        })


class TodoUpdateView(APIView):
    def put(self, request, id):
        todo = Todo.objects.get(id=id)
        todo.title = request.data["title"]
        todo.memo = request.data["memo"]
        todo.priority = request.data["priority"]
        todo.save()
        return Response(status=200)


class AllTodoListView(APIView):
    def get(self, request):
        todos = Todo.objects.all()
        return JsonResponse({
            "todos": [
                {
                    "id": todo.id,
                    "title": todo.title,
                    "memo": todo.memo,
                    "priority": todo.priority,
                    "author": todo.author.name,
                } for todo in todos
            ]
        })
