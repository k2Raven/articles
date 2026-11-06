from django import forms
from django.forms import widgets
from webapp.validators import at_last_10, MinLengthValidator

from webapp.models import Article




# class ArticleForm(forms.Form):
#     title = forms.CharField(max_length=50, validators=[at_last_10], required=True, label='Заголовок')
#     author = forms.CharField(max_length=60, validators=[MinLengthValidator(5)], required=True, label='Автор')
#     content = forms.CharField(max_length=5000, widget=widgets.Textarea, required=True, label='Контент')

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'author', 'content', 'status', 'tags']