import random

from django.shortcuts import render
from django.views import View

import hero.models as heromodels


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
        for i in range (1):
            temp = {"name": i, "description": "Test descriptions", "href": "http://127.0.0.1:8000/heroes/pudge/"}
            results.append(temp)

        context = {'search_input': search_input, 'results': results}
        return render(request, self.template_name, context)
