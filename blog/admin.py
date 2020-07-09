from django.contrib import admin
from .models import Article, Tag


class ArticleAdmin(admin.ModelAdmin):
    model = Article
    filter_horizontal = ('tags', )


admin.site.register(Tag)
admin.site.register(Article, ArticleAdmin)
