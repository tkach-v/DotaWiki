import json
from io import BytesIO

import requests
from PIL import Image

from hero.models import Hero, Ability, AbilityType


def run():
    with open("hero/abilities_all.json") as f1:
        heroes_ability = json.load(f1)

    Ability.objects.all().delete()

    for row in heroes_ability:
        print(row['hero_name'])

        ow = Hero.objects.get(name=row['hero_name'])

        for ab in row['abilities']:
            ab_type, created = AbilityType.objects.get_or_create(name=ab["type"])

            ability = Ability(
                owner=ow,
                name=ab['name'],
                description=ab['description'],
                type=ab_type,
                generic_details=ab['generic_details'],
                specific_details=ab['specific_details'],
                cooldown=ab['cooldown'],
                mana_cost=ab['mana_cost']
            )

            response = requests.get(ab['image_url'])
            image = Image.open(BytesIO(response.content))
            image_io = BytesIO()
            image.save(image_io, format='PNG')
            image_io.seek(0)
            ability.image_url.save(ab['name'].lower().replace(" ", "_") + '.png', image_io)

            ability.save()
