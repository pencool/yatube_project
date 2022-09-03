from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse('Привет это главная страница '
                        'проекта Yatube, оставайся тут, скоро будет весело!')


def group_posts(request, text):
    return HttpResponse(f'Пока здесь видно только это: {text}')
