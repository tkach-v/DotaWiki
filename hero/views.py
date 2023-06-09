from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.http import JsonResponse

from .models import *


class HeroDetail(DetailView):
    model = Hero
    template_name = 'hero/heroes_detail.html'
    context_object_name = 'hero'
    slug_url_kwarg = 'slug'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        hero = self.object
        heroes = Hero.objects.order_by('name')

        abilities = hero.ability_set.all()
        cosmetics = hero.cosmetic_set.all()
        context['abilities'] = abilities
        context['cosmetics'] = cosmetics

        next_hero = heroes.filter(name__gt=hero.name).first()
        if not next_hero:
            next_hero = heroes.first()

        prev_hero = heroes.filter(name__lt=hero.name).last()
        if not prev_hero:
            prev_hero = heroes.last()

        context['next_hero'] = next_hero
        context['prev_hero'] = prev_hero
        return context


class HeroesList(ListView):
    model = Hero
    template_name = 'hero/heroes_list.html'
    context_object_name = 'heroes'
    queryset = Hero.objects.order_by('name')

    def dispatch(self, request, *args, **kwargs):
        if 'X-Requested-With' in request.headers and request.headers['X-Requested-With'] == 'XMLHttpRequest':
            if request.method == 'GET':
                complexity = request.GET.get("complexity")
                primary_ability = request.GET.get("primary_ability")

                # Query the database based on the parameters
                queryset = Hero.objects.order_by('name')
                if complexity:
                    queryset = queryset.filter(complexity=complexity)
                if primary_ability:
                    primary_stat = PrimaryStat.objects.get(name=primary_ability)
                    queryset = queryset.filter(primary_stat=primary_stat)

                # Serialize the queryset to JSON and return the response
                heroes = list(queryset.values())
                return JsonResponse({"context": heroes})

            return JsonResponse({'status': 'Invalid request'}, status=400)
        else:
            return super().dispatch(request, *args, **kwargs)
