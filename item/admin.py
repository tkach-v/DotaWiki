from django.contrib import admin
from .models import *

admin.site.register(Item)
admin.site.register(Shareable)
admin.site.register(Disassemble)
admin.site.register(Availability)
admin.site.register(TypeGlobal)
admin.site.register(TypeSpecific)
admin.site.register(ItemAbility)
