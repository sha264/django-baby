from todo import views
from django.urls import path
from .views import TodoAddView, TodoDeleteView, TodoUpdateView, TodoListView, AllTodoListView
from django.conf.urls import url

urlpatterns = [
    path('test/', views.test),
    path("add/", TodoAddView.as_view()),
    path("delete/<int:id>", TodoDeleteView.as_view()),
    path("update/<int:id>", TodoUpdateView.as_view()),
    path("list/<int:id>", TodoListView.as_view()),
    path("list/", AllTodoListView.as_view()),
]
