import jsonfield
from django.db import models
from django.utils.text import slugify


class Item(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50, blank=True, null=True)
    image_url = models.ImageField(upload_to='photos/items')
    description = models.CharField(max_length=200)
    lore_description = models.CharField(max_length=200, blank=True)
    type_global = models.ForeignKey('TypeGlobal', on_delete=models.CASCADE)
    type_specific = models.ForeignKey('TypeSpecific', on_delete=models.CASCADE)
    cost = models.CharField(max_length=100, null=True)
    sell_value = models.CharField(max_length=100, null=True)
    bonus = models.CharField(max_length=300, null=True, blank=True)
    shareable = models.ForeignKey('Shareable', on_delete=models.CASCADE)
    disassemble = models.ForeignKey('Disassemble', on_delete=models.CASCADE)
    availability = models.ForeignKey('Availability', on_delete=models.CASCADE)
    recipe = models.ManyToManyField('self', blank=True, symmetrical=False)
    need_recipe = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)


class Shareable(models.Model):
    name = models.CharField(max_length=100, null=True)

    def __str__(self):
        return str(self.name)


class Disassemble(models.Model):
    name = models.CharField(max_length=100, null=True)

    def __str__(self):
        return str(self.name)


class Availability(models.Model):
    name = models.CharField(max_length=100, null=True)

    def __str__(self):
        return str(self.name)


class TypeGlobal(models.Model):
    name = models.CharField(max_length=100, null=True)

    def __str__(self):
        return str(self.name)


class TypeSpecific(models.Model):
    name = models.CharField(max_length=100, null=True)

    def __str__(self):
        return str(self.name)


class ItemAbility(models.Model):
    owner = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=300, null=True)
    cooldown = models.CharField(max_length=100, null=True)
    manacost = models.CharField(max_length=100, null=True)
    details = jsonfield.JSONField(blank=True, null=True)
    ability_type = models.ForeignKey('AbilityType', on_delete=models.CASCADE)
    affects = models.ForeignKey('Affects', on_delete=models.CASCADE)
    damage = models.ForeignKey('Damage', on_delete=models.CASCADE)


class AbilityType(models.Model):
    name = models.CharField(max_length=100, null=True)


class Affects(models.Model):
    name = models.CharField(max_length=100, null=True)


class Damage(models.Model):
    name = models.CharField(max_length=100, null=True)



