#-*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.utils import timezone
from .models import Post
from django.shortcuts import render, get_object_or_404


def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {"posts": posts})


def japanese_garden(request):
    japanese_garden_img = "/media/yaponskij_sad.jpg"
    return render(request, "blog/japanese_garden.html", {"japanese_garden_img": japanese_garden_img})


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})