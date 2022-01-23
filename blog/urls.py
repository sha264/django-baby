from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('sample',views.blog_sample),
]