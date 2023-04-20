from django.db import models


class Hero(models.Model):
    name = models.CharField(max_length=50)
    primary_stat = models.CharField(max_length=50) # change to ForeignKey
    description_short = models.TextField()
    description_long = models.TextField()
    attack_type = models.CharField(max_length=50) # change to ForeignKey
    complexity = models.IntegerField()
    image_url_small = models.ImageField(upload_to="photos/%Y/%m/%d/") # change directory
    image_url_large = models.ImageField(upload_to="photos/%Y/%m/%d/") # change directory
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
    left_10 = models.CharField(max_length=50)
    right_10 = models.CharField(max_length=50)
    left_15 = models.CharField(max_length=50)
    right_15 = models.CharField(max_length=50)
    left_20 = models.CharField(max_length=50)
    right_20 = models.CharField(max_length=50)
    left_25 = models.CharField(max_length=50)
    right_25 = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class PrimaryStat(models.Model):
    name = models.CharField(max_length=50)
