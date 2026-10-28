from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse

from webapp.forms import ArticleForm
from  webapp.models import Article
from django.http import HttpResponseRedirect, HttpResponseNotFound, Http404

def index_view(request):
    context = {
        'articles': Article.objects.all()
    }
    return render(request, 'index.html', context)

def article_view(request, pk):
    # try:
    #     article = Article.objects.get(pk=pk)
    # except Article.DoesNotExist:
    #     # return HttpResponseNotFound('Article not found')
    #     raise Http404('Article not found')
    article = get_object_or_404(Article, pk=pk)
    return render(request, 'article_view.html', {'article': article})



def article_create_view(request):

    if request.method == 'GET':
        form = ArticleForm()
        return render(request, 'create_article.html', {'form': form})
    elif request.method == 'POST':
        form = ArticleForm(data= request.POST)
        if form.is_valid():
            article = form.save()
            return redirect('article_view', pk=article.id)
        else:
            return render(request, 'create_article.html', {'form': form})


def article_update_view(request, pk):
    article = get_object_or_404(Article, pk=pk)
    if request.method == 'GET':
        form = ArticleForm(instance=article)
        return render(request, 'update_article.html', {'article': article, 'form': form})
    elif request.method == 'POST':
        form = ArticleForm(data=request.POST, instance=article)
        if form.is_valid():
            form.save()
            return redirect('article_view', pk=article.id)
        else:
            return render(request, 'update_article.html', {'article': article, 'form': form})



def article_delete_view(request, pk):
    article = get_object_or_404(Article, pk=pk)
    if request.method == "GET":
        return render(request, 'delete_article.html', {'article': article})
    elif request.method == "POST":
        article.delete()
        return redirect('article_list')