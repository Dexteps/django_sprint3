from datetime import datetime

from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, get_object_or_404

from .models import Category, Post


def index(request: HttpRequest) -> HttpResponse:
    """Функция вызова шаблона (главная страница)."""
    posts = Post.objects.select_related(
        'author',
        'category',
        'location'
    ).filter(
        is_published=True,
        pub_date__date__lte=datetime.now(),
        category__is_published=True
    ).order_by('-pub_date')[0:5]
    return render(request, 'blog/index.html', {'post_list': posts})


def post_detail(request: HttpRequest, post_id: int) -> HttpResponse:
    """Функция вызова шаблона (полная информация постов)."""
    post = get_object_or_404(Post.objects.select_related(
        'author',
        'category',
        'location'
    ),
        is_published=True,
        category__is_published=True,
        pub_date__date__lte=datetime.now(),
        pk=post_id
    )
    return render(request, 'blog/detail.html', {'post': post})


def category_posts(request: HttpRequest, category_slug: str) -> HttpResponse:
    """Функция вызова шаблона (категории)."""
    category = get_object_or_404(
        Category,
        is_published=True,
        slug=category_slug
    )
    post_list = category.category_posts.filter(
        pub_date__date__lte=datetime.now(),
        is_published=True
    )
    return render(request, 'blog/category.html', {
        'category': category,
        'post_list': post_list
    }
    )
