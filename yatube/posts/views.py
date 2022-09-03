from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render


def index(request):
    return render(request, 'posts/index.html')


def group_posts(request, text):
    return HttpResponse(f'Пока здесь видно только это: {text}')
