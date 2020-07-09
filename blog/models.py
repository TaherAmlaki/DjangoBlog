from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=30)
    slug = models.SlugField(max_length=50, unique=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


class Article(models.Model):
    title = models.TextField()
    tags = models.ManyToManyField(Tag, related_name="article_tags")
    short_description = models.TextField(default="")
    html_name = models.CharField(max_length=100)
    date_created = models.DateField()
    git_url = models.URLField(max_length=200, blank=True, null=True)
    slug = models.SlugField(max_length=50, unique=True, default="")

    class Meta:
        ordering = ['-date_created']

    def __str__(self):
        return self.slug




