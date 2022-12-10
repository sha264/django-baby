from django.urls import path
from django.http import HttpResponse
from .views import blog_list,blog_like,blog_get

app_name = 'blog'



urlpatterns = [
    path('list/', blog_list),
    path('like/', blog_like),
    path('get/<int:id>/', blog_get),
]
