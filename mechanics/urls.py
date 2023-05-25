from django.urls import path
from .views import *

app_name = 'mechanics'

urlpatterns = [
    path('', mechanics_view, name='mechanics'),
]