from django.urls import path
from webapp.views import index_view, about_view, article_create_view, article_view, article_delete_view

urlpatterns = [
    path('', index_view),
    path('about/', about_view),
    path('articles/add/', article_create_view),
    path('article/', article_view),

    path('article/delete/', article_delete_view),
]