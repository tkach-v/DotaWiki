from django.urls import path
from .views import *

app_name = 'hero'

urlpatterns = [
    path('', HeroesList.as_view(), name='hero_list'),
    path('<slug:slug>/', HeroDetail.as_view(), name='hero_detail'),
    path('test/', index)
]