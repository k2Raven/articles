from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse, reverse_lazy
from django.views.generic import FormView, ListView, DetailView, CreateView, UpdateView, DeleteView

from webapp.forms import ArticleForm
from  webapp.models import Article


class IndexView(ListView):
    template_name = 'index.html'
    context_object_name = 'articles'
    model = Article
    ordering = ['-created_at']
    paginate_by = 3
    paginate_orphans = 3


class ArticleView(DetailView):
    template_name = 'article_view.html'
    model = Article


class ArticleCreateView(CreateView):
    template_name = 'create_article.html'
    model = Article
    form_class = ArticleForm

    def get_success_url(self):
        return reverse('article_view', kwargs={'pk': self.object.pk})


class ArticleUpdateView(UpdateView):
    template_name = 'update_article.html'
    model = Article
    form_class = ArticleForm

    def get_success_url(self):
        return reverse('article_view', kwargs={'pk': self.object.pk})



class ArticleDeleteView(DeleteView):
    template_name = 'delete_article.html'
    model = Article
    success_url = reverse_lazy('article_list')

    # def get(self, *args, **kwargs):
    #     return self.delete(*args, **kwargs)