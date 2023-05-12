import json
from io import BytesIO

import PIL
import requests
from PIL import Image

from hero.models import Hero, PrimaryStat, AttackType


def run():
    with open("hero/heroes_all.json") as f1:
        heroes = json.load(f1)

    Hero.objects.all().delete()

    for row in heroes:
        print(row['name'])

        pry_stat, created = PrimaryStat.objects.get_or_create(name=row['primary_stat'])
        att_type, created = AttackType.objects.get_or_create(name=row['attack_type'])

        hero = Hero(
            name=row['name'],
            primary_stat=pry_stat,
            description_short=row['description_short'],
            description_long=row['description_long'],
            attack_type=att_type,
            complexity=row['complexity'],
            image_url_small='',
            image_url_large='',
            health=row['health'],
            mana=row['mana'],
            strength=row['strength'],
            strength_increase=row['strength_increase'],
            agility=row['agility'],
            agility_increase=row['agility_increase'],
            intelligence=row['intelligence'],
            intelligence_increase=row['intelligence_increase'],
            damage=row['damage'],
            attack_delay=row['attack_delay'],
            attack_range=row['attack_range'],
            flight_speed=row['flight_speed'],
            armor=row['armor'],
            magic_resistance=row['magic_resistance'],
            move_speed=row['move_speed'],
            turn_speed=row['turn_speed'],
            vision=row['vision'],
            talent_left_10=row['left_10'],
            talent_right_10=row['right_10'],
            talent_left_15=row['left_15'],
            talent_right_15=row['right_15'],
            talent_left_20=row['left_20'],
            talent_right_20=row['right_20'],
            talent_left_25=row['left_25'],
            talent_right_25=row['right_25']
        )
        # Load images from the Internet and save it
        try:
            response_small = requests.get(row['image_url_small'])
            image = Image.open(BytesIO(response_small.content))
            image_io_small = BytesIO()
            image.save(image_io_small, format='PNG')
            image_io_small.seek(0)
            hero.image_url_small.save(row['name'].lower().replace(" ", "_") + '_small' + '.png', image_io_small)
        except PIL.UnidentifiedImageError:
            print("No image small in", row['name'])
            pass

        try:
            response_large = requests.get(row['image_url_large'])
            image = Image.open(BytesIO(response_large.content))
            image_io_large = BytesIO()
            image.save(image_io_large, format='PNG')
            image_io_large.seek(0)
            hero.image_url_large.save(row['name'].lower().replace(" ", "_") + '_large' + '.png', image_io_large)
        except PIL.UnidentifiedImageError:
            print("No image large in", row['name'])
            pass

        hero.save()
