from django.urls import path
from .views import *

app_name = 'item'

urlpatterns = [
    path('test/', index),
    path('test2/', index2)
]