from django.http import HttpResponse
from django.views.generic import ListView
from django.shortcuts import render
from .models import *


def index(request):
    return render(request, "hero/index.html")


class MyModelListView(ListView):
    model = Hero
    template_name = 'hero/heroes_list.html'
    context_object_name = 'my_model_list'