from django.contrib import admin

from .models import Promocode

# Register your models here.

class PromocodeAdmin(admin.ModelAdmin):
    pass

admin.site.register(Promocode, PromocodeAdmin)
