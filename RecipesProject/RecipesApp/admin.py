from .models import  Recipe
from django.contrib import admin

admin.site.register(Recipe)


class RecipeAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}

