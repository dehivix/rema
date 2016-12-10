#-*- coding: utf8 -*-
"""
Django settings for rema project.

Generated by 'django-admin startproject' using Django 1.8.5.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
from django.conf.global_settings import TEMPLATE_CONTEXT_PROCESSORS as TCP

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'zxkh28uusgdky1dlon%&5jqx9dzw9y6kan!56%-t9ewjow!v@6'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
CSRF_COOKIE_DOMAIN = None
ALLOWED_HOSTS = []

LANGUAGE_CODE = 'es-ve'

#SUIT CONFIG
SUIT_CONFIG = {
    'SEARCH_URL': '/admin/general/personas/',
    # header
     'ADMIN_NAME': 'REMA - Registro Electoral Ministerial Automatizado',
     'HEADER_DATE_FORMAT': 'l, j. F Y',
     'HEADER_TIME_FORMAT': 'H:i',

    # forms
     'SHOW_REQUIRED_ASTERISK': True,  # Default True
     'CONFIRM_UNSAVED_CHANGES': True, # Default True

    # menu
     'MENU_OPEN_FIRST_CHILD': True, # Default True
    # 'MENU_EXCLUDE': ('auth.group',),
     'MENU': (
        '-',
         {'label': 'Acceso y Seguridad', 'icon':'icon-lock', 'models': (
             {'url': '/admin/auth/user/', 'label': 'Usuarios'},
             {'url': '/admin/auth/group/', 'label': 'Grupos'},
         )},
         '-',
         {'label': 'General', 'url':'','icon':'icon-globe','models': (
             {'url': '/admin/general/personas/', 'label': 'Personas'},
             {'url': '/admin/general/autoridades', 'label': 'Autoridades'},
         )},
        '-',
        '-',
         {'label': 'Cargos', 'icon':'icon-briefcase', 'models': (
             {'url': '/admin/general/cargos/', 'label': 'Cargos'},
             {'url': '/admin/general/autoridades', 'label': 'Autoridades'},
         )},
         '-',
         {'label': 'Reportes' , 'url':'', 'icon':'icon-print'},
         {'label': u'Estadísticos', 'models': (
             {'url': '/reporte/resultados/', 'label': 'Gráfico de resultado de elecciones', 'permissions': ('estudiantes.reportes_inscrito')},
         )},
         '-',
     ),

    # misc
    # 'LIST_PER_PAGE': 15
}




# Application definition

INSTALLED_APPS = (
    'suit',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'general',
    'votacion',
    #'candidatos',
    'materialize',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
)

ROOT_URLCONF = 'rema.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]


TEMPLATE_CONTEXT_PROCESSORS=(

    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.debug',
    "django.contrib.messages.context_processors.messages",
    'django.core.context_processors.media',
    'django.core.context_processors.request',
    'django.core.context_processors.csrs',
)

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
    'django.template.loaders.eggs.Loader',
)
TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    os.path.join(os.getcwd(), 'templates'),
    os.path.join(os.getcwd(), 'templates/admin'),
)


WSGI_APPLICATION = 'rema.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

STATIC_ROOT =os.path.join(os.getcwd(), 'static/')
STATIC_URL = '/static/'

MEDIA_ROOT = 'votacion/static/'

MEDIA_URL = '/media/'

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    #'django.contrib.staticfiles.finders.DefaultStorageFinder',
)
