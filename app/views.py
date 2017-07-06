# -*- coding: utf-8 -*-
from django.shortcuts import render,get_object_or_404
from app.models import Author,Tag,Article,Category,Comment
from .forms import CommentForm
def get_blogs(request):
    ctx = {
        'article_list':Article.objects.all().filter(status='p').order_by('created_time')
        }
    return render(request,'app/index.html',ctx)

def get_detail(request,article_id):
    article = get_object_or_404(Article,id=article_id)
    if request.method == 'GET':
        form = CommentForm()
    else:
        form = CommentForm(request.POST)
        if form.is_valid():
            cleaned_data = form.cleaned_data
            cleaned_data['article'] = article
            Comment.objects.create(**cleaned_data)
            
    ctx = {
        'article':article,
        'comments':article.comment_set.all().order_by('-created_time'),
        'form':form
        }
    return render(request,'app/detail.html',ctx)