from django import forms
from django.forms import widgets
from webapp.validators import at_last_10, MinLengthValidator

from webapp.models import Article


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'author', 'content', 'status', 'tags']


class SimpleSearchForm(forms.Form):
    search = forms.CharField(max_length=100, required=False,
                             widget=widgets.TextInput(attrs={'class': 'form-control me-2'}), label='Найти')
