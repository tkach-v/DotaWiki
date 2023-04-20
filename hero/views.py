from django.http import HttpResponse
from django.shortcuts import render
from .models import *


def index(request):
    temp = Hero.objects.get(pk=1)
    context = {
       "name": temp.name,
       "small": temp.image_url_small,
       "large": temp.image_url_large
    }
    return render(request, "hero/index.html", context=context)
