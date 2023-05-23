from django.views import View
from django.shortcuts import render
import random


class HomeView(View):
    template_name = 'home/index.html'
    video_list = ['video1.mp4', 'video2.mp4', 'video3.mp4', 'video4.mp4', 'video5.mp4', 'video6.mp4']

    def get(self, request):
        random_video = random.choice(self.video_list)
        context = {'random_video': random_video}
        return render(request, self.template_name, context)



