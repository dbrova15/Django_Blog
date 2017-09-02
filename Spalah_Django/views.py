# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect
from django.shortcuts import render, get_object_or_404
from django.contrib.auth import authenticate
from django.contrib.auth import login, logout
from django.utils import timezone
from .models import Post  # , ExampleModel
# from .models import handle_uploaded_file
from .forms import PostForm  # , ImageUploadForm
# from .forms import UploadFileForm
from django.http import HttpResponseRedirect, HttpResponse
from .models import News
from .forms import LoginForm


def news_list(request):
    context = {'news_list': News.objects.all()}
    return render(request, 'blog/news.html', context)


def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {"posts": posts})


def japanese_garden(request):
    japanese_garden_img = "/media/yaponskij_sad.jpg"
    return render(request, "blog/japanese_garden.html", {"japanese_garden_img": japanese_garden_img})


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})


@login_required
def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        print(request.POST)
        print("\n", request.FILES)
        if form.is_valid():
            print("Bla bla")
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
        else:
            print(form.is_valid())
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {
        'form': form
    })


def post_del(request, pk):
    post = get_object_or_404(Post, pk=pk)
    query = post.delete()
    return redirect("/", request, query)


@login_required
def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES, instance=post)
        print(request.POST)
        print("\n", request.FILES)
        if form.is_valid():
            print("Bla bla")
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})


def log_in(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            if form.get_user():
                login(request, form.get_user())
                return HttpResponseRedirect('/')
    else:
        form = LoginForm()
    return render(request, 'blog/login.html', {'form': form})


def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/')


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return HttpResponseRedirect('/')
    else:
        form = UserCreationForm()
    return render(request, 'blog/signup.html', {'form': form})

