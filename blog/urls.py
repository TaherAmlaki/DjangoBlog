from django.urls import path
from .views import ArticleListView, ArticleDetailView, TagArticleListView


urlpatterns = [
    path("", ArticleListView.as_view(), name='blog-home'),
    path("articles/<str:slug>/", ArticleDetailView.as_view(), name="article-detail"),
    path("subject/<str:slug>/", TagArticleListView.as_view(), name="tag-articles"),
]
