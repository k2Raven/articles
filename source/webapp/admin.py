from django.contrib import admin
from webapp.models import Article, Comment

admin.site.register(Comment)


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'content', 'author')
    list_filter = ('author',)
    search_fields = ('title', 'content')
    fields = ('id', 'title', 'content', 'status', 'author', 'created_at', 'updated_at')
    readonly_fields = ('id', 'created_at', 'updated_at')
