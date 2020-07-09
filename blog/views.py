from django.views.generic import ListView, DetailView
from django.shortcuts import get_object_or_404
from collections import Counter
from .models import Article, Tag


class ArticleListView(ListView):
    model = Article
    template_name = "blog/blog.html"
    context_object_name = "articles"
    ordering = ['-date_created']
    paginate_by = 5

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        tags = list(Tag.objects.filter(article_tags__in=Article.objects.all()))
        context['AllTags'] = dict(Counter(tags).most_common())
        return context


class ArticleDetailView(DetailView):
    model = Article
    template_name = "blog/article_base.html"
    context_object_name = "article"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        self.template_name = context[self.context_object_name].html_name
        return context


class TagArticleListView(ListView):
    model = Article
    template_name = "blog/tag_blog.html"
    context_object_name = "articles"
    paginate_by = 5

    def get_queryset(self):
        tag = get_object_or_404(Tag, slug=self.kwargs.get("slug"))
        return Article.objects.filter(tags=tag).order_by('-date_created')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        tag = get_object_or_404(Tag, slug=self.kwargs.get("slug"))
        context['TagName'] = tag.name
        return context

