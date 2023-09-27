from django.shortcuts import render, redirect, get_object_or_404
from .models import Recipe
from .forms import RecipeForm
from RecipesProject.DrinksApp.models import Drinks


def recipe_detail(request, slug):
    recipe = get_object_or_404(Recipe, slug=slug)

    return render(request, 'recipe_detail.html', {'recipe': recipe})


class RecipeDetailView(Recipe):
    model = Recipe
    template_name = "recipe_detail.html"


def recipes(request):
    recipe = Recipe.objects.all()
    drinks = Drinks.objects.all()
    return render(request, "recipes.html", {'recipe': recipe, 'drinks': drinks})


def create_recipe(request):
    if request.method == "POST":
        form = RecipeForm(request.POST, request.FILES)
        if form.is_valid():
            recipe = form.save(commit=False)
            recipe.author = request.user
            recipe.save()
            return redirect('recipe_detail', slug=recipe.slug)
    else:
        form = RecipeForm()

    return render(request, 'create_recipe.html', {'form': form})


def edit_recipes(request, slug):
    recipe = get_object_or_404(Recipe, slug=slug)

    if request.method == "POST":
        form = RecipeForm(request.POST, request.FILES, instance=recipe)
        if form.is_valid():
            form.save()
            return redirect('recipe_detail', slug=recipe.slug)
    else:
        form = RecipeForm(instance=recipe)

    return render(request, 'edit_recipe.html', {'form': form, 'recipe': recipe})


def destroy_recipes(request, slug):
    recipe = get_object_or_404(Recipe, slug=slug)

    if request.method == "POST":
        recipe.delete()
        return redirect('home')

    return render(request, 'templates/delete_recipe_confirm.html', {'recipe': recipe})
