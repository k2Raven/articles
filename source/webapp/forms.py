from django import forms
from django.forms import widgets


class ArticleForm(forms.Form):
    title = forms.CharField(max_length=50, required=True, label='Заголовок')
    author = forms.CharField(max_length=60, required=True, label='Автор')
    content = forms.CharField(max_length=5000, widget=widgets.Textarea, required=True, label='Контент')
