from django.http import HttpRequest, HttpResponse
from django.shortcuts import render


def about(request: HttpRequest) -> HttpResponse:
    """Функция вызова шаблона (про нас)."""
    return render(request, 'pages/about.html')


def rules(request: HttpRequest) -> HttpResponse:
    """Функция вызова шаблона (наши правила)."""
    return render(request, 'pages/rules.html')
