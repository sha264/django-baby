from django.contrib import admin
from django.http.response import HttpResponse
from django.urls import path

def top_page_func(request):
    print('Hello World!!!')
    return HttpResponse('Hello World!!!')


def animal_page_func(request, animal_name):
    print(animal_name)
    return HttpResponse('このページは' + animal_name + 'についてです！')


def dog_page_func(request):
    return HttpResponse('このページは犬についてです！犬は賢くていいですね！！')


def cat_page_func(request):
    return HttpResponse('このページは猫についてです！猫はかわいいですね！')


def handle_number(request, number):
    print(number)
    return HttpResponse('あなたは'+str(number)+'番を入力しました！！！')


def search_func(request):
    search_word = request.GET['q']
    print(search_word)
    return HttpResponse('あなたは'+search_word+'を検索しました！！！')


def square_func(request, number):
    answer = number ** 2
    return HttpResponse(str(number)+'の2乗は'+str(answer)+'です！！！')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello', top_page_func),
    path('animal/dog', dog_page_func),
    path('animal/cat', cat_page_func),
    path('animal/<str:animal_name>', animal_page_func),
    path('num/<int:number>', handle_number),
    path('search/', search_func),
    path('square/<int:number>', square_func),
]