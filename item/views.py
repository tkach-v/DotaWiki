from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.http import JsonResponse, HttpResponse
from .models import *


class ItemList(ListView):
    model = Item
    template_name = 'item/items_list.html'
    context_object_name = 'items'
    queryset = Item.objects.order_by('name')


class ItemDetail(DetailView):
    model = Item
    template_name = 'item/items_detail.html'
    context_object_name = 'item'
    slug_url_kwarg = 'slug'


def index2(request):
    return render(request, 'item/items_detail.html')
