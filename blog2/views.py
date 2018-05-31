from django.shortcuts import render
# Create your views here.
from . import models


def index(request):
    #获取单条数据
    #article = models.Article.objects.get(pk=1)

    #获取全部数据
    articles = models.Article.objects.all()
    return render(request,'blog2/index.html',{'articles':articles})


def article_page(request,article_id):
    article = models.Article.objects.get(pk=article_id)
    return  render(request,'blog2/article_info.html',{'article':article})

def article_edit(request,article_id):
    if str(article_id) == '0':
       return render(request,'blog2/article_edit.html')
    article = models.Article.objects.get(pk=article_id)
    return render(request, 'blog2/article_edit.html', {'article': article})


def edit_action(request):
    title = request.POST.get('title','TITLE')
    content = request.POST.get('content','CONTENT')
    article_id = request.POST.get('article_id', '0')
    if article_id == '0':
        models.Article.objects.create(title=title,content=content)
        articles = models.Article.objects.all()
        return render(request, 'blog2/index.html', {'articles': articles})
    article = models.Article.objects.get(pk=article_id)
    article.title = title
    article.content = content
    article.save()
    return render(request, 'blog2/article_info.html', {'article': article})