from django.urls import path
from .views import *

app_name = 'item'

urlpatterns = [
    path('', ItemList.as_view(), name='item_list'),
    path('<slug:slug>/', ItemDetail.as_view(), name='item_detail')
]