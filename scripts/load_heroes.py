from hero.models import *
import json


def run():
    with open("hero/heroes_all.json") as f1:
        heroes = json.load(f1)

    for hero in heroes:
        print(hero["name"])
