from django.shortcuts import render


def mechanics_view(request):
    return render(request, 'mechanics/mechanics.html')
