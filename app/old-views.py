# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from app.models import Article,Author,Category
from django.views import generic
import markdown
# Create your views here.
class IndexView(generic.ListView):
    template_name = 'app/index.html'
    def get_queryset(self):
        article_list = Article.objects.filter(status='p')
        for article in article_list:
            article.context = markdown.markdown(article.context,)
        return article_list
    def get_context_data(self, **kwargs):
        kwargs['category_list'] = Category.objects.all().order_by('name')
        return super(IndexView, self).get_context_data(**kwargs)
    
class CategoryView(generic.ListView):
    template_name = 'app/index.html'
    def get_queryset(self):
        article_list = Article.objects.filter(category=self.kwargs['cate_id'], status='p')
        for article in article_list:
            article.context = markdown.markdown(article.context,)
        return article_list
    def get_context_data(self, **kwargs):
        kwargs['category_list'] = Category.objects.all().order_by('name')
        name = get_object_or_404(Category, pk=self.kwargs['cate_id'])
        kwargs['cate_name'] = name

        return super(CategoryView, self).get_context_data(**kwargs)
    
class ArticleDetailView(generic.DetailView):
    model = Article
    template_name = 'blog/detail.html'
    
    
    