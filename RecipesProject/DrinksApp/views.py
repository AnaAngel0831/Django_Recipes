from django.shortcuts import render, redirect, get_object_or_404
from .models import Drinks
from .forms import DrinksForm


def drink_detail(request, slug):

    drinks = get_object_or_404(Drinks, slug=slug)
    return render(request, 'drink_detail.html', {'drinks': drinks})


class DrinkDetailView(Drinks):
    model = Drinks
    template_name = "drink_detail.html"


def drink(request):
    drinks = Drinks.objects.all()
    return render(request, "recipes.html", {"drink": drinks})


def create_drink(request):
    if request.method == "POST":
        form = DrinksForm(request.POST, request.FILES)
        if form.is_valid():
            drinks = form.save(commit=False)
            drinks.author = request.user
            drinks.save()
            return redirect('drink_detail', slug=drinks.slug)
    else:
        form = DrinksForm()

    return render(request, 'create_drink.html', {'form': form})


def edit_drinks(request, slug):  # Change the view name to edit_drinks
    drinks = get_object_or_404(Drinks, slug=slug)

    if request.method == "POST":
        form = DrinksForm(request.POST, request.FILES, instance=drink)
        if form.is_valid():
            form.save()
            return redirect('drink_detail', slug=drinks.slug)
    else:
        form = DrinksForm(instance=drinks)

    return render(request, 'edit_drink.html', {'form': form, 'drinks': drinks})


def destroy_drinks(request, slug):
    drinks = get_object_or_404(Drinks, slug=slug)

    if request.method == "POST":
        drinks.delete()
        return redirect('home')  # Redirect to home or any other page after deletion

    return render(request, 'delete_drink_confirm.html', {'drinks': drinks})
