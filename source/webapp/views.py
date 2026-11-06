from typing import Any

from django.http import HttpRequest, HttpResponseBase, HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.views.generic import View, TemplateView, FormView
from django.views.generic.edit import _FormT

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



class ArticleCreateView(FormView):
    template_name = 'create_article.html'
    form_class = ArticleForm

    def form_valid(self, form):
        article = form.save()
        return redirect('article_view', pk=article.id)


class ArticleUpdateView(FormView):
    template_name = 'update_article.html'
    form_class = ArticleForm

    def dispatch(self, request, *args, **kwargs):
        self.article = get_object_or_404(Article, pk=kwargs.get('pk'))
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['article'] = self.article
        return context

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['instance'] = self.article
        return kwargs

    def form_valid(self, form):
        self.article = form.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('article_view', kwargs={'pk': self.article.pk})




def article_delete_view(request, pk):
    article = get_object_or_404(Article, pk=pk)
    if request.method == "GET":
        return render(request, 'delete_article.html', {'article': article})
    elif request.method == "POST":
        article.delete()
        return redirect('article_list')