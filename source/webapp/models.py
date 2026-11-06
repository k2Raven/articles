from django.db import models
from slugify import slugify


class Status(models.Model):
    title = models.CharField(max_length=20, unique=True, null=False, blank=False, verbose_name='Название')
    slug = models.SlugField(max_length=20, unique=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Дата обновления")

    def __str__(self):
        return f'{self.pk} - {self.title}'

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)



class Article(models.Model):
    title = models.CharField(max_length=50, null=False, blank=False, verbose_name="Заголовок")
    content = models.TextField(max_length=5000, null=False, blank=False, verbose_name="Контент")
    status = models.ForeignKey('webapp.Status', related_name='articles', null=True, on_delete=models.CASCADE,
                               verbose_name='Статус')
    author = models.CharField(max_length=60, null=False, blank=False, default='Anonymous', verbose_name="Автор")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Дата обновления")
    tags = models.ManyToManyField('webapp.Tag', related_name='articles', through='webapp.ArticleTag',
                                      through_fields=('article', 'tag'), blank=True, verbose_name='Теги')

    def __str__(self):
        return f'{self.pk} - {self.title}'


class Comment(models.Model):
    article = models.ForeignKey('webapp.Article', related_name='comments', on_delete=models.CASCADE,
                                verbose_name='Статья')
    text = models.TextField(max_length=600, verbose_name='Комментарий')
    author = models.CharField(max_length=60, null=False, blank=False, default='Anonymous', verbose_name="Автор")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Дата обновления")

    def __str__(self):
        return f'{self.pk} - {self.text[:20]}'


class Tag(models.Model):
    name = models.CharField(max_length=40, verbose_name="Название")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Дата обновления")

    def __str__(self):
        return self.name


class ArticleTag(models.Model):
    article = models.ForeignKey('webapp.Article', related_name='article_tags', on_delete=models.CASCADE,
                                verbose_name='Статья')
    tag = models.ForeignKey('webapp.Tag', related_name='tag_articles', on_delete=models.CASCADE,
                            verbose_name='Тег')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Дата обновления")

    def __str__(self):
        return f'{self.article.title} - {self.tag.name}'
