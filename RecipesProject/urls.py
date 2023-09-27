from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('recipes/', include("RecipesProject.RecipesApp.urls")),
    path('users/', include("RecipesProject.UsersApp.urls")),
    path('drinks/', include("RecipesProject.DrinksApp.urls")),

]
