from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.http import JsonResponse, HttpResponse
from .models import *


def index(request):
    return render(request, 'item/items_list.html')


def index2(request):
    return render(request, 'item/items_detail.html')
