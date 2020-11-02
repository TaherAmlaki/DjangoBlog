from django.views.generic import ListView, DetailView
from django.views.generic.edit import FormMixin
from django.urls import reverse
from django.contrib import messages
from django.shortcuts import get_object_or_404
from collections import Counter
from .models import Article, Tag
from .MyForms import CommentForm
from profile_app.models import AboutMe


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


class ArticleDetailView(FormMixin, DetailView):
    model = Article
    template_name = "blog/article_base.html"
    context_object_name = "article"
    form_class = CommentForm

    def get_success_url(self):
        return reverse('article-detail', kwargs={"slug": self.object.slug})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        self.template_name = context[self.context_object_name].html_name
        context['about_me'] = AboutMe.objects.first()
        context["form"] = self.get_form()  #CommentForm(initial={"article": self.object})
        context['comments'] = self.object.comments.filter(reply=None)
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()

        if form.is_valid():
            name = form.cleaned_data['name']

            comment = form.save(commit=False)
            comment.article = self.object

            reply_id = request.POST.get("reply_id")
            if reply_id is not None:
                reply_obj = self.object.comments.filter(id=int(reply_id)).first()
                if reply_obj is not None:
                    comment.reply = reply_obj

            comment.save()

            if reply_id is not None:
                messages.success(request, f"Thank you {name}, your reply is added.")
            else:
                messages.success(request, f"Thank you {name}, your comment is added.")
            return super(ArticleDetailView, self).form_valid(form)
        else:
            messages.error(request, f"Sorry. Something went wrong, could not save your comment.")
            return self.form_invalid(form)


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
        context['ActiveTags'] = [tag.name]

        all_tags = list(Tag.objects.filter(article_tags__in=Article.objects.all()))
        context['AllTags'] = dict(Counter(all_tags).most_common())
        return context

