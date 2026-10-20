from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse

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
        return render(request, 'create_article.html')
    elif request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        author = request.POST.get('author')
        article = Article.objects.create(title=title, content=content, author=author)

        # url = reverse('article_view', kwargs={'pk': article.pk})
        # return HttpResponseRedirect(url)
        return redirect('article_view', pk=article.id)