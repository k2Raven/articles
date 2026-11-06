from django.urls import path
from webapp.views import IndexView, article_create_view, ArticleView, article_update_view, article_delete_view, \
    ArticlesStatusView

urlpatterns = [
    path('', IndexView.as_view(), name='article_list'),
    path('articles/<slug:slug>/', ArticlesStatusView.as_view(), name='articles_by_status'),
    path('article/add/', article_create_view, name='article_create'),
    path('article/<int:pk>/', ArticleView.as_view(), name='article_view'),
    path('article/<int:pk>/update/', article_update_view, name='article_update'),
    path('article/<int:pk>/delete/', article_delete_view, name='article_delete'),
]