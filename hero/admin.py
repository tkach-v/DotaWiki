from .models import *
from django.contrib import admin


class AbilityAdmin(admin.ModelAdmin):
    search_fields = ['name', 'description']


admin.site.register(Ability, AbilityAdmin)
admin.site.register(Hero)
admin.site.register(AttackType)
admin.site.register(PrimaryStat)
admin.site.register(AbilityType)
admin.site.register(Cosmetic)
