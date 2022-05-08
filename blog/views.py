from django.http import HttpResponse
from django.shortcuts import render


def blog_sample(request):
    return HttpResponse("blogアプリの作成完了！")


def render_html(request):
    return render(request, "blog/index.html", {})


def render_html_with_variables(request):
    return render(request, "blog/use_variables.html", {"food": "餃子"})


def render_html_with_if_sentenses(request):
    return render(request, "blog/use_if_sentences.html", {"food": "回鍋肉"})


def render_html_with_for_sentenses(request):
    return render(request, "blog/use_for_sentences.html", {"foods": ["餃子", "回鍋肉"]})
