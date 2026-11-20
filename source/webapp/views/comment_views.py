from django.shortcuts import get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.urls import reverse
from django.views.generic import CreateView, UpdateView, DeleteView

from webapp.forms import CommentForm
from webapp.models import Article, Comment


class CommentCreateView(LoginRequiredMixin, CreateView):
    template_name = 'comment/create.html'
    model = Comment
    form_class = CommentForm

    def form_valid(self, form):
        article = get_object_or_404(Article, pk=self.kwargs.get('pk'))
        form.instance.article = article
        form.instance.author = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('webapp:article_view', kwargs={'pk': self.object.article.pk})


class CommentUpdateView(PermissionRequiredMixin, UpdateView):
    template_name = 'comment/update.html'
    model = Comment
    form_class = CommentForm
    permission_required = 'webapp.change_comment'

    def get_success_url(self):
        return reverse('webapp:article_view', kwargs={'pk': self.object.article.pk})


class CommentDeleteView(PermissionRequiredMixin, DeleteView):
    template_name = 'comment/delete.html'
    model = Comment
    permission_required = 'webapp.delete_comment'

    def get_success_url(self):
        return reverse('webapp:article_view', kwargs={'pk': self.object.article.pk})
