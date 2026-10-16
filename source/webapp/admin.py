from django.contrib import admin
from webapp.models import Article

# admin.site.register(Article)

# class ArticleAdmin(admin.ModelAdmin):
#     pass
#
# admin.site.register(Article, ArticleAdmin)

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'content', 'author')
    list_filter = ('author',)
    search_fields = ('title', 'content')
    fields = ('id', 'title', 'content', 'author', 'created_at', 'updated_at')
    # exclude = []
    readonly_fields = ('id', 'created_at', 'updated_at')
