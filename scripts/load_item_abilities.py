import json
from item.models import ItemAbility, AbilityType, Affects, Damage, Item


def run():
    with open("item/item_abilities_all.json") as f1:
        items_ability = json.load(f1)

    ItemAbility.objects.all().delete()

    for row in items_ability:
        print(row['item_name'])

        ow = Item.objects.get(name=row['item_name'])

        for ab in row['abilities']:
            ab_type, created = AbilityType.objects.get_or_create(name=ab["ability"])
            af, created = Affects.objects.get_or_create(name="affects")
            dmg, created = Damage.objects.get_or_create(name="damage")

            ability = ItemAbility(
                owner=ow,
                name=ab['name'],
                description=ab['description'],
                cooldown=ab['cooldown'],
                manacost=ab['manacost'],
                details=ab['details'],
                ability_type=ab_type,
                affects=af,
                damage=dmg
            )
            ability.save()

