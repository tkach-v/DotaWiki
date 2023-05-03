from django.shortcuts import render

def home_func(request):
    return render(request, 'home/home.html')
