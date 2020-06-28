from django.http import HttpResponse
from django.shortcuts import render
from rss.apps.rss_news.models import Post


# Create your views here.

def index(request):

    posts = reversed(Post.objects.all())

    context = {
        'posts': posts
    }

    return render(request, "index.html", context)

def post(request,rss_news_id):

    try:
        post = Post.objects.get(id=rss_news_id)
        result = post.text
    except Post.DoesNotExist:
        result = " Net takogo posta"

    return HttpResponse(str(result))

def signup (request):
    return render(request, "signup.html")