from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.shortcuts import get_object_or_404

from .models import *


class ItemList(ListView):
    template_name = 'item/items_list.html'
    context_object_name = 'items'

    def get_queryset(self):
        type_global = get_object_or_404(TypeGlobal, name='Basics')
        return Item.objects.filter(type_global=type_global).order_by('name')


class ItemDetail(DetailView):
    model = Item
    template_name = 'item/items_detail.html'
    context_object_name = 'item'
    slug_url_kwarg = 'slug'


def index2(request):
    return render(request, 'item/items_detail.html')
