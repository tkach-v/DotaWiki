import json
from io import BytesIO

import PIL
import requests
from PIL import Image

from item.models import Item, Shareable, Disassemble, Availability, TypeGlobal, TypeSpecific


def run():
    with open("item/items_all.json") as f1:
        items = json.load(f1)

    Item.objects.all().delete()
    TypeSpecific.objects.all().delete()
    Availability.objects.all().delete()

    for row in items:
        print(row['name'])

        shareable_val, created = Shareable.objects.get_or_create(name=row['shareable'])
        disassemble_val, created = Disassemble.objects.get_or_create(name=row['disassemble'])
        availability_val, created = Availability.objects.get_or_create(name=row['availability'])
        type_global_val, created = TypeGlobal.objects.get_or_create(name=row['type_global'])
        if type_global_val.name == 'Neutral':
            type_specific_val, created = TypeSpecific.objects.get_or_create(name=row['type_specific'][:6])
        else:
            type_specific_val, created = TypeSpecific.objects.get_or_create(name=row['type_specific'])

        item = Item(
            name=row['name'],
            image_url='',
            description=row['description'],
            lore_description=row['lore_description'],
            type_global=type_global_val,
            type_specific=type_specific_val,
            cost=row['cost'],
            sell_value=row['sell_value'],
            bonus=row['bonus'],
            shareable=shareable_val,
            disassemble=disassemble_val,
            availability=availability_val
        )
        # Load images from the Internet and save it
        try:
            response = requests.get(row['image_url'])
            image = Image.open(BytesIO(response.content))
            image_io = BytesIO()
            image.save(image_io, format='PNG')
            image_io.seek(0)
            item.image_url.save(row['name'].lower().replace(" ", "_") + '.png', image_io)
        except PIL.UnidentifiedImageError:
            print("No image small in", row['name'])
            pass

        item.save()
