from django.urls import path
from .views import *

app_name = 'creeps'

urlpatterns = [
    path('', creeps_view, name='creeps'),
]