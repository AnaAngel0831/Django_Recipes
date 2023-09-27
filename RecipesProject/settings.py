import os
from pathlib import Path

from RecipesProject import UsersApp, DrinksApp

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'django-insecure-9rg$9pz+9!$0v$x_3jlf7jofk3)w%igdc2vsx*1-y63k!=iwb7'
DEBUG = True
# AUTHENTICATION_BACKENDS = [
#     'django.contrib.auth.backends.ModelBackend',
# ]
ALLOWED_HOSTS = []

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'RecipesProject',
    'RecipesProject.RecipesApp',
    'RecipesProject.UsersApp',
    'RecipesProject.DrinksApp',
    'crispy_forms',
    'django_extensions',
]
CRISPY_TEMPLATE_PACK = 'bootstrap4'

# AUTHENTICATION_BACKENDS = 'django.contrib.auth.backends.ModelBackend'

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')


ROOT_URLCONF = 'RecipesProject.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],  # No need to specify individual paths
        'APP_DIRS': False,  # Automatically look for templates in each app
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                # 'RecipesProject.RecipesApp.context_processors.profile_pic',
            ],
            'loaders': [
                ('django.template.loaders.filesystem.Loader', [
                    'RecipesProject.RecipesApp.templates',
                    'RecipesProject.UsersApp.templates',
                    'RecipesProject.DrinksApp.templates',
                ]),
                'django.template.loaders.app_directories.Loader',
            ],
        },
    },
]

WSGI_APPLICATION = 'RecipesProject.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

AUTH_USER_MODEL = "UsersApp.User"

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / "RecipesApp/static"]

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
