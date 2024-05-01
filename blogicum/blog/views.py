from django.http import HttpRequest, HttpResponse
from django.shortcuts import get_object_or_404, render
from django.utils.timezone import now

from .common import filter_objects
from .constants import MAX_POSTS_PAGE
from .models import Category, Post


def index(request: HttpRequest) -> HttpResponse:
    """Функция вызова шаблона (главная страница)."""
    posts = filter_objects(Post.objects)[:MAX_POSTS_PAGE]
    return render(request, 'blog/index.html', {'post_list': posts})


def post_detail(request: HttpRequest, post_id: int) -> HttpResponse:
    """Функция вызова шаблона (полная информация постов)."""
    post = get_object_or_404(filter_objects(Post.objects), pk=post_id)
    return render(request, 'blog/detail.html', {'post': post})


def category_posts(request: HttpRequest, category_slug: str) -> HttpResponse:
    """Функция вызова шаблона (категории)."""
    category = get_object_or_404(
        Category,
        is_published=True,
        slug=category_slug
    )
    post_list = category.posts.filter(
        pub_date__date__lte=now(),
        is_published=True
    )
    return render(request, 'blog/category.html', {
        'category': category,
        'post_list': post_list
    }
    )
