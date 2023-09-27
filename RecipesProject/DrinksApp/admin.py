from .models import Drinks
from django.contrib import admin

admin.site.register(Drinks)


class DrinkAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
