import json
from item.models import Item


def run():
    with open("item/items_all.json") as f1:
        items = json.load(f1)

    for row in items:
        item = Item.objects.get(name=row['name'])
        if len(row['recipe']) > 0:
            recipe_items = row['recipe']
            if 'Recipe' in recipe_items:
                print(row['name'])
                item.need_recipe = True
                item.save()
            recipe_objects = Item.objects.filter(name__in=recipe_items)
            item.recipe.set(recipe_objects)
            item.save()
