from django.views.generic import ListView, DetailView
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from django.db.models import F


from .models import *


class ItemList(ListView):
    template_name = 'item/items_list.html'
    context_object_name = 'items'
    try:
        type_global = get_object_or_404(TypeGlobal, name='Basics')
        queryset = Item.objects.filter(type_global=type_global).order_by('name')
    except:
        queryset = Item.objects.all().order_by('name')

    def dispatch(self, request, *args, **kwargs):
        if 'X-Requested-With' in request.headers and request.headers['X-Requested-With'] == 'XMLHttpRequest':
            if request.method == 'GET':
                type_global_name = request.GET.get("type-global")
                type_specific_name = request.GET.get("type-specific")

                # Query the database based on the parameters
                queryset = Item.objects.order_by('name')
                type_global = TypeGlobal.objects.get(name=type_global_name)
                queryset = queryset.filter(type_global=type_global)

                if type_specific_name != "All":
                    type_specific = TypeSpecific.objects.get(name=type_specific_name)
                    queryset = queryset.filter(type_specific=type_specific)

                # Serialize the queryset to JSON and return the response
                items = list(queryset.values('name', 'image_url', 'slug', 'cost', specific_name=F("type_specific__name")))
                print(items[0])
                return JsonResponse({"context": items})
            return JsonResponse({'status': 'Invalid request'}, status=400)
        else:
            return super().dispatch(request, *args, **kwargs)


class ItemDetail(DetailView):
    model = Item
    template_name = 'item/items_detail.html'
    context_object_name = 'item'
    slug_url_kwarg = 'slug'
