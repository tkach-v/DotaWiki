from django.contrib import admin
from .models import *
from django.contrib import admin

class AbilityAdmin(admin.ModelAdmin):
    search_fields = ['name', 'description']  # Додайте поля, по яких потрібно робити пошук


admin.site.register(Ability, AbilityAdmin)
admin.site.register(Hero)
admin.site.register(AttackType)
admin.site.register(PrimaryStat)
admin.site.register(AbilityType)
admin.site.register(Cosmetic)