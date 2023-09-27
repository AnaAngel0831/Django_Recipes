from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name="home"),
    path('login/', views.user_login, name="user_login"),
    path('register/', views.register, name="register"),
    path('settings/<int:id>', views.settings, name="settings"),
    path('logout/', views.user_logout, name='user_logout'),
    path(r'^password/$', views.change_password, name='change_password'),
    path('users/', views.users),
    path('profile/', views.profile, name='profile'),
    path('show/', views.show, name='show'),
    path('edit_user/<int:id>', views.edit_user, name='edit_user'),
    path('delete_user/<int:id>', views.delete_user, name='delete_user'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
