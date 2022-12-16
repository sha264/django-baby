from django.urls import path
from django.http import HttpResponse
from .views import todo_add,todo_delete,todo_list,todo_init,TodoAddView,TodoDeleteView,get_tags_from_todo,get_todos_from_tag,get_todo_including_user_name,get_todos_from_user

app_name = 'todo'

urlpatterns = [
    path('1/', todo_list),
    path("todoadd/", TodoAddView.as_view()),
    path("tododelete/<int:id>/", TodoDeleteView.as_view()),
    path('tag/<int:id>/', get_todos_from_tag),
    path('todo/<int:id>/', get_tags_from_todo),
    path('username/<int:id>/',get_todo_including_user_name),
    path('user/<int:id>/',get_todos_from_user),
]
