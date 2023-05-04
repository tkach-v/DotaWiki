from django.urls import path

from .views import *

app_name = 'hero'
urlpatterns = [
    path('', HeroesList.as_view(), name='hero_list')
]