from django.db import models


class Status(models.Model):
    title = models.CharField(max_length=20, unique=True, null=False, blank=False, verbose_name='Название')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Дата обновления")

    def __str__(self):
        return f'{self.pk} - {self.title}'
