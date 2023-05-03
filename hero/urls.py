from django.urls import path

from .views import *

urlpatterns = [
    path('', index, name='hero_app'),
    path('heroes/', MyModelListView.as_view())
]