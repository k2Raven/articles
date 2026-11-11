from django import forms
from django.forms import widgets


class SimpleSearchForm(forms.Form):
    search = forms.CharField(max_length=100, required=False,
                             widget=widgets.TextInput(attrs={'class': 'form-control me-2'}), label='Найти')
