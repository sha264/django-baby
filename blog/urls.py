from django.urls import path
from . import views

app_name = "blog"

urlpatterns = [
    path("sample", views.blog_sample),
    path("render_html", views.render_html),
    path("render_html_with_variables", views.render_html_with_variables),
    path("render_html_with_if_sentences", views.render_html_with_if_sentenses),
    path("render_html_with_for_sentences", views.render_html_with_for_sentenses),
]
