from typing import Any

from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import View, TemplateView

from webapp.forms import ArticleForm
from  webapp.models import Article


class IndexView(View):
    def get(self, request, *args, **kwargs):
        context = {
            'articles': Article.objects.all()
        }
        return render(request, 'index.html', context)


# class AboutView(TemplateView):
#     template_name = 'about.html'

class ArticleView(TemplateView):
    template_name = 'article_view.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['article'] = get_object_or_404(Article, pk=kwargs.get('pk'))
        return context




def article_create_view(request):

    if request.method == 'GET':
        form = ArticleForm()
        return render(request, 'create_article.html', {'form': form})
    elif request.method == 'POST':
        form = ArticleForm(data= request.POST)
        if form.is_valid():
            title = form.cleaned_data.get('title')
            content = form.cleaned_data.get('content')
            author = form.cleaned_data.get('author')
            article = Article.objects.create(title=title, content=content, author=author)
            return redirect('article_view', pk=article.id)
        else:
            return render(request, 'create_article.html', {'form': form})


def article_update_view(request, pk):
    article = get_object_or_404(Article, pk=pk)
    if request.method == 'GET':
        form = ArticleForm(initial={'title': article.title, 'content': article.content, 'author': article.author})
        return render(request, 'update_article.html', {'article': article, 'form': form})
    elif request.method == 'POST':
        form = ArticleForm(data=request.POST)
        if form.is_valid():
            article.title = form.cleaned_data.get('title')
            article.content = form.cleaned_data.get('content')
            article.author = form.cleaned_data.get('author')
            article.save()
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