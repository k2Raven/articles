from urllib.parse import urlencode

from django.db.models import Q
from django.shortcuts import get_object_or_404
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from webapp.forms import ArticleForm, SimpleSearchForm, CommentForm
from webapp.models import Article, Comment


class IndexView(ListView):
    template_name = 'index.html'
    context_object_name = 'articles'
    model = Article
    ordering = ['-created_at']
    paginate_by = 3
    # paginate_orphans = 3

    def get_search_form(self):
        return SimpleSearchForm(self.request.GET)

    def get_search_value(self):
        if self.form.is_valid():
            return self.form.cleaned_data['search']
        return None

    def get(self, request, *args, **kwargs):
        self.form = self.get_search_form()
        self.search_value = self.get_search_value()
        return super().get(request, *args, **kwargs)

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['form'] = self.form
        if self.search_value:
            context['query'] = urlencode({'search': self.search_value})
            context['search'] = self.search_value
        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        if self.search_value:
            query = (Q(title__icontains=self.search_value) |
                     Q(content__icontains=self.search_value) |
                     Q(author__icontains=self.search_value))
            queryset = queryset.filter(query)
        return queryset

class ArticleView(DetailView):
    template_name = 'article_view.html'
    model = Article

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comments'] = self.object.comments.order_by('-created_at')
        return context


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


class CommentCreateView(CreateView):
    template_name = 'create_comment.html'
    model = Comment
    form_class = CommentForm

    def form_valid(self, form):
        article = get_object_or_404(Article, pk=self.kwargs.get('pk'))
        form.instance.article = article
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('article_view', kwargs={'pk': self.object.article.pk})


class CommentUpdateView(UpdateView):
    template_name = 'update_comment.html'
    model = Comment
    form_class = CommentForm

    def get_success_url(self):
        return reverse('article_view', kwargs={'pk': self.object.article.pk})


class CommentDeleteView(DeleteView):
    template_name = 'delete_comment.html'
    model = Comment

    def get_success_url(self):
        return reverse('article_view', kwargs={'pk': self.object.article.pk})