from django.shortcuts import render
from django.http import HttpResponse
from .models import Products


def index(request):
    s = Products.objects.all()[::]

    return HttpResponse(s)
