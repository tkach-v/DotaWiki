from django.shortcuts import render


def creeps_view(request):
    return render(request, 'creeps/creeps.html')
