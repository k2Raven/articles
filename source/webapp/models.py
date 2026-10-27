from django.db import models


class Status(models.Model):
    title = models.CharField(max_length=20, unique=True, null=False, blank=False, verbose_name='Название')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Дата обновления")

    def __str__(self):
        return f'{self.pk} - {self.title}'


class Article(models.Model):
    title = models.CharField(max_length=50, null=False, blank=False, verbose_name="Заголовок")
    content = models.TextField(max_length=5000, null=False, blank=False, verbose_name="Контент")
    status = models.ForeignKey('webapp.Status', related_name='articles', null=True, on_delete=models.CASCADE, verbose_name='Статус')
    author = models.CharField(max_length=60, null=False, blank=False, default='Anonymous', verbose_name="Автор")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Дата обновления")

    def __str__(self):
        return f'{self.pk} - {self.title}'
