from django.http import HttpResponse
from django.views.generic import ListView
from django.shortcuts import render
from .models import *


def index(request):
    return render(request, "hero/index.html")


class HeroesList(ListView):
    model = Hero
    template_name = 'hero/heroes_list.html'
    context_object_name = 'heroes'
    queryset = Hero.objects.order_by('name')

    def get_queryset(self):
        queryset = super().get_queryset()
        complexity = self.request.GET.get('complexity')
        if complexity:
            queryset = queryset.filter(complexity=complexity)
        return queryset
