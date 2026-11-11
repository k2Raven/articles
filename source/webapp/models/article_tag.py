from django.db import models


class ArticleTag(models.Model):
    article = models.ForeignKey('webapp.Article', related_name='article_tags', on_delete=models.CASCADE,
                                verbose_name='Статья')
    tag = models.ForeignKey('webapp.Tag', related_name='tag_articles', on_delete=models.CASCADE, verbose_name='Тег')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Дата обновления")
