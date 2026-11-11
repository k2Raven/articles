from django import forms
from django.forms import widgets

from webapp.models import Article, Comment


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'author', 'content', 'status', 'tags']


class SimpleSearchForm(forms.Form):
    search = forms.CharField(max_length=100, required=False,
                             widget=widgets.TextInput(attrs={'class': 'form-control me-2'}), label='Найти')

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text', 'author']