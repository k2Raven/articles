from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.views.generic import CreateView, UpdateView, DeleteView

from webapp.forms import CommentForm
from webapp.models import Article, Comment


class CommentCreateView(CreateView):
    template_name = 'comment/create.html'
    model = Comment
    form_class = CommentForm

    def form_valid(self, form):
        article = get_object_or_404(Article, pk=self.kwargs.get('pk'))
        form.instance.article = article
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('article_view', kwargs={'pk': self.object.article.pk})


class CommentUpdateView(UpdateView):
    template_name = 'comment/update.html'
    model = Comment
    form_class = CommentForm

    def get_success_url(self):
        return reverse('article_view', kwargs={'pk': self.object.article.pk})


class CommentDeleteView(DeleteView):
    template_name = 'comment/delete.html'
    model = Comment

    def get_success_url(self):
        return reverse('article_view', kwargs={'pk': self.object.article.pk})
