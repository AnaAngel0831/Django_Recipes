from django.apps import AppConfig


class UserConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'users'
    def ready(self):
        import self.signals


class RecipesappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'RecipesProject.RecipesApp'

