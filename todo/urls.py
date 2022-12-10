from django.urls import path
from django.http import HttpResponse
from .views import todo_add,todo_delete,todo_list,todo_init,TodoAddView,TodoDeleteView

app_name = 'todo'



urlpatterns = [
    path('1/', todo_list),
    path("todoadd/", TodoAddView.as_view()),
    path("tododelete/<int:id>/", TodoDeleteView.as_view()),
]
