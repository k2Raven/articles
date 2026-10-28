from django import forms
from django.core.exceptions import ValidationError
from django.forms import widgets


def validate_author(value):
    if "@" in value:
        raise ValidationError('В имени автора не может быть данного символа "@"')


class ArticleForm(forms.Form):
    title = forms.CharField(max_length=50, min_length=3, required=True,
                            widget=widgets.Input(attrs={'class': 'form-control'}), label='Заголовок')
    author = forms.CharField(max_length=60, validators=[validate_author, ],
                             widget=widgets.Input(attrs={'class': 'form-control'}), required=True, label='Автор')
    content = forms.CharField(max_length=5000, widget=widgets.Textarea(attrs={'class': 'form-control'}), required=True,
                              label='Контент')

    def clean_title(self):
        title = self.cleaned_data.get('title')
        # if "*" in title:
        #     raise ValidationError('В имени автора не может быть данного символа "*"')
        if title:
            title = title.replace('*', '#')
        return title

    def clean(self):
        title = self.cleaned_data.get('title')
        content = self.cleaned_data.get('content')
        if title and content and title.lower() == content.lower():
            raise ValidationError('Название и контент не могут быть одинаковыми')
