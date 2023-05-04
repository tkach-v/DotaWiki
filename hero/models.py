from django.db import models
from django.utils.text import slugify
import jsonfield


class Hero(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50, blank=True, null=True)
    primary_stat = models.ForeignKey('PrimaryStat', on_delete=models.CASCADE)
    description_short = models.TextField()
    description_long = models.TextField()
    attack_type = models.ForeignKey("AttackType", on_delete=models.CASCADE)
    complexity = models.IntegerField()
    image_url_small = models.ImageField(upload_to="photos/heroes")
    image_url_large = models.ImageField(upload_to="photos/heroes")
    health = models.CharField(max_length=50)
    mana = models.CharField(max_length=50)
    strength = models.CharField(max_length=50)
    strength_increase = models.CharField(max_length=50)
    agility = models.CharField(max_length=50)
    agility_increase = models.CharField(max_length=50)
    intelligence = models.CharField(max_length=50)
    intelligence_increase = models.CharField(max_length=50)
    damage = models.CharField(max_length=50)
    attack_delay = models.CharField(max_length=50)
    attack_range = models.CharField(max_length=50)
    flight_speed = models.CharField(max_length=50)
    armor = models.CharField(max_length=50)
    magic_resistance = models.CharField(max_length=50)
    move_speed = models.CharField(max_length=50)
    turn_speed = models.CharField(max_length=50)
    vision = models.CharField(max_length=50)
    talent_left_10 = models.CharField(max_length=100)
    talent_right_10 = models.CharField(max_length=100)
    talent_left_15 = models.CharField(max_length=100)
    talent_right_15 = models.CharField(max_length=100)
    talent_left_20 = models.CharField(max_length=100)
    talent_right_20 = models.CharField(max_length=100)
    talent_left_25 = models.CharField(max_length=100)
    talent_right_25 = models.CharField(max_length=100)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class PrimaryStat(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class AttackType(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Ability(models.Model):
    owner = models.ForeignKey("Hero", on_delete=models.PROTECT)
    name = models.CharField(max_length=50)
    description = models.TextField()
    image_url = models.ImageField(upload_to='photos/abilities')
    type = models.ForeignKey("AbilityType", on_delete=models.PROTECT)
    generic_details = jsonfield.JSONField(blank=True, null=True)
    specific_details = jsonfield.JSONField(blank=True, null=True)
    cooldown = models.CharField(max_length=50, null=True)
    mana_cost = models.CharField(max_length=50, null=True)

    def __str__(self):
        return self.name


class AbilityType(models.Model):
    name = models.CharField(max_length=50, null=True)

    def __str__(self):
        return str(self.name)


