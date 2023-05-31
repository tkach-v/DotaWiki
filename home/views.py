import random

from django.shortcuts import render
from django.views import View

import hero.models as heromodels
import item.models as itemmodels


class HomeView(View):
    template_name = 'home/index.html'
    video_list = ['video1.mp4', 'video2.mp4', 'video3.mp4', 'video4.mp4', 'video5.mp4', 'video6.mp4']

    def get(self, request):
        random_video = random.choice(self.video_list)
        context = {'random_video': random_video}
        return render(request, self.template_name, context)


class SearchView(View):
    template_name = 'home/search.html'

    def get(self, request):
        search_input = request.GET['search']
        results = []

        # Додати обробку пошуку для розділів сайту
        if str(search_input).lower() in "heroes":
            name = "Heroes"
            description = "This tab provides information about the heroes in Dota 2. You can explore various heroes, their abilities, attributes, and lore."
            href = "heroes"
            results.append({"name": name, "description": description, "href": href})

        if str(search_input).lower() in "items":
            name = "Items"
            description = "Objects that can be purchased on the game map. Items increase a hero's properties, and grant them special abilities and effects. Neutral items can be found by killing neutral creeps."
            href = "items"
            results.append({"name": name, "description": description, "href": href})

        if str(search_input).lower() in "creeps":
            name = "Creeps"
            description = "In the Creeps tab, you can delve into the world of creeps and neutrals in Dota 2. Creeps are non-player units that spawn regularly and populate the lanes and jungles."
            href = "creeps"
            results.append({"name": name, "description": description, "href": href})

        if str(search_input).lower() in "mechanics":
            name = "Mechanics"
            description = "The Mechanics tab focuses on the intricate gameplay mechanics and systems in Dota 2. Gain insights into the underlying mechanics that shape the game and influence decision-making, strategy, and tactics."
            href = "mechanics"
            results.append({"name": name, "description": description, "href": href})


        # пошук в базі даних
        heroes_results = heromodels.Hero.objects.filter(name__icontains=search_input)
        for hero in heroes_results:
            name = hero.name
            description = hero.description_short
            href = "heroes/" + hero.slug
            results.append({"name": name, "description": description, "href": href})

        items_results = itemmodels.Item.objects.filter(name__icontains=search_input)
        for item in items_results:
            name = item.name
            description = item.description
            href = "items/" + item.slug
            results.append({"name": name, "description": description, "href": href})

        cosmetics_results = heromodels.Cosmetic.objects.filter(name__icontains=search_input)
        for cosmetic in cosmetics_results:
            name = cosmetic.name
            description = f"Cosmetic item for {cosmetic.owner.name}"
            href = "heroes/" + cosmetic.owner.slug
            results.append({"name": name, "description": description, "href": href})

        context = {'search_input': search_input, 'results': results}
        return render(request, self.template_name, context)
