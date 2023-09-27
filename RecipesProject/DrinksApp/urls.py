from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

urlpatterns = [
    path('<int:pk>', views.DrinkDetailView, name="drink_detail"),
    path('drinks/<slug:slug>/', views.drink_detail, name='drink_detail'),
    path('create_drink/', views.create_drink, name='create_drink'),
    path('edit_drink/<slug:slug>/', views.edit_drinks, name='edit_drink'),
    path('drinks/<slug:slug>/delete/', views.destroy_drinks, name='destroy_drinks'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
