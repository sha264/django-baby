from django.http import HttpResponse

def blog_sample(request):
    return HttpResponse('blogアプリの作成完了！')