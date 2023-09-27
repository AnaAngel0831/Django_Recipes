from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

urlpatterns = [

    path("recipes/", views.recipes, name="recipes"),
    path("<int:pk>", views.RecipeDetailView, name="recipe_detail"),
    path('recipes/<slug:slug>/', views.recipe_detail, name='recipe_detail'),
    path('create_recipe/', views.create_recipe, name='create_recipe'),
    path('edit_recipe/<slug:slug>/', views.edit_recipes, name='edit_recipes'),
    path('recipes/<slug:slug>/delete/', views.destroy_recipes, name='destroy_recipes'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
