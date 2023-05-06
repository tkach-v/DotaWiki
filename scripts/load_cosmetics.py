import json
from io import BytesIO

import requests
from PIL import Image

from hero.models import Hero, Cosmetic


def run():
    with open("hero/cosmetics_all.json") as f1:
        heroes_cosmetics = json.load(f1)

    Cosmetic.objects.all().delete()

    for row in heroes_cosmetics:
        print(row['hero_name'])

        ow = Hero.objects.get(name=row['hero_name'])

        for cosm in row['cosmetics']:

            cosmetic = Cosmetic(
                owner=ow,
                name=cosm['name'],
            )

            response = requests.get(cosm['image_url'])
            image = Image.open(BytesIO(response.content))
            image_io = BytesIO()
            image.save(image_io, format='PNG')
            image_io.seek(0)
            cosmetic.image_url.save(cosm['name'].lower().replace(" ", "_") + '.png', image_io)

            cosmetic.save()
