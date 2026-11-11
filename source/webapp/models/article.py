from django.db import models
from webapp.validators import MinLengthValidator


class Article(models.Model):
    title = models.CharField(max_length=50, null=False, blank=False, verbose_name="Заголовок")
    content = models.TextField(max_length=5000, validators=[MinLengthValidator(20)], null=False, blank=False,
                               verbose_name="Контент")
    status = models.ForeignKey('webapp.Status', related_name='articles', null=True, on_delete=models.CASCADE,
                               verbose_name='Статус')
    author = models.CharField(max_length=60, null=False, blank=False, default='Anonymous', verbose_name="Автор")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Дата обновления")
    tags = models.ManyToManyField('webapp.Tag', related_name='articles', through='webapp.ArticleTag',
                                  through_fields=('article', 'tag'), blank=True, verbose_name='Теги')

    def __str__(self):
        return f'{self.pk} - {self.title}'
