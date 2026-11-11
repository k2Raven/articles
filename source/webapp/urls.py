from django.urls import path
from webapp.views import IndexView, ArticleCreateView, ArticleView, ArticleUpdateView, ArticleDeleteView, CommentCreateView

urlpatterns = [
    path('', IndexView.as_view(), name='article_list'),
    path('article/add/', ArticleCreateView.as_view(), name='article_create'),
    path('article/<int:pk>/', ArticleView.as_view(), name='article_view'),
    path('article/<int:pk>/update/', ArticleUpdateView.as_view(), name='article_update'),
    path('article/<int:pk>/delete/', ArticleDeleteView.as_view(), name='article_delete'),
    path('article/<int:pk>/comment/add/', CommentCreateView.as_view(), name='comment_create'),
]