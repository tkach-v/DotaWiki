from item.models import ItemAbility, AbilityType, Affects, Damage, Item


def run():
    ItemAbility.objects.all().delete()
    Affects.objects.all().delete()
    Damage.objects.all().delete()
    AbilityType.objects.all().delete()