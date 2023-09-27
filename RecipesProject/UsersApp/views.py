from django.contrib import messages
from django.contrib.auth.forms import PasswordChangeForm
from django.shortcuts import render, redirect
from .models import User, UserProfile
from .forms import UsersForm, UserForm, UserProfileForm, EditUserForm, CustomLoginForm
from django.contrib.auth import logout, login, authenticate, update_session_auth_hash
from ..DrinksApp.models import Drinks
from RecipesProject.RecipesApp.models import Recipe


def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Your password was successfully updated!')
            return redirect('change_password')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'change_password.html', {
        'form': form
    })


def settings(request, id):
    user = User.objects.get(id=id)
    user_profile = UserProfile.objects.get(user=user)

    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=user)
        profile_form = UserProfileForm(request.POST, request.FILES, instance=user_profile)
        if user_form.is_valid():
            user_form.save()

        if profile_form.is_valid():
            profile_form.save()
    else:
        user_form = UserForm(instance=user)
        profile_form = UserProfileForm(instance=user_profile)

    return render(request, 'settings.html', {'user_form': user_form, 'profile_form': profile_form, 'user': user})


def user_logout(request):
    logout(request)
    return redirect('user_login')


def user_login(request):
    if request.method == 'POST':
        form = CustomLoginForm(request.POST)

        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate(username=email, password=password)
            print(user)
            if user is not None:
                login(request, user)
                return redirect('recipes')  # Redirect to the dashboard after successful login
            else:
                return render(request, 'login.html', {'form': form, 'error_message': 'Invalid email or password'})
    else:
        form = CustomLoginForm()

    return render(request, 'login.html', {'form': form})


def register(request):
    registered = False

    if request.method == "POST":
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid:
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user

            if 'profile_pic' is request.FILES:
                profile.profile_pic = request.FILES['profile_pic']

            profile.save()
            registered = True
            return render(request, 'login.html'
                          , {'user_form': user_form, 'profile_form': profile_form,
                             'registered': registered})
        else:
            print(user_form.errors, profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = UserProfileForm()

    return render(request, 'register.html'
                  , {'user_form': user_form, 'profile_form': profile_form,
                     'registered': registered})


def profile(request):
    user = request.user
    recipes = Recipe.objects.filter(author=user)
    drinks = Drinks.objects.filter(author=user)
    return render(request, 'profile.html', {'recipes': recipes, 'drinks': drinks})


def home(request):
    return render(request, "home.html")


def users(request):
    if request.method == "POST":
        form = UsersForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return UsersForm('/show')
            except:
                pass
    else:
        form = UsersForm()
    return render(request, 'index.html', {'form': form})


def show(request):
    user = request.user
    if user.is_staff:
        users = User.objects.all()
        return render(request, "show.html", {'users': users})
    else:
        recipes = Recipe.objects.all()
        drinks = Drinks.objects.all()
        return render(request, "recipes.html", {'recipes': recipes, 'drinks': drinks})


def edit_user(request, id):
    user = User.objects.get(id=id)

    if request.method == 'POST':
        form = EditUserForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('show')  # Redirect to the user list page after successful edit
    else:
        form = EditUserForm(instance=user)

    return render(request, 'edit_user.html', {'form': form, 'user': user})


def delete_user(request, id):
    user = User.objects.get(id=id)
    if request.method == "POST":
        user.delete()
        return redirect('/show')
    return render(request, 'delete_user_confirm.html', {'user': user})
