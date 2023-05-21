from django.shortcuts import render, HttpResponse
from channels.celery import add
def home(request):
    a = add.delay(1,2)
    return HttpResponse(f'hii{a}')