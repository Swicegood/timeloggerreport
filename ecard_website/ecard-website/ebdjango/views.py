from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse


def index(request):
    return HttpResponse("<H1>Hello, world. You're at the eCard index.</H1>")