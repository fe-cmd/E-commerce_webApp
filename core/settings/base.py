"""
Django settings for core project.

Generated by 'django-admin startproject' using Django 4.0.4.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.0/ref/settings/
"""

import os
import environ
from dotenv import load_dotenv
from pathlib import Path
import django_heroku

CSRF_TRUSTED_ORIGINS = [' https://engisole-commercestore.herokuapp.com ']

env = environ.Env()
environ.Env.read_env()

dotenv_path = os.path.join(os.path.dirname(__file__), 'data.env')
load_dotenv(dotenv_path)
BASE_DIR = Path(__file__).resolve().parent.parent.parent

SECRET_KEY =  str(os.getenv('SECRET_KEY'))

# social auth configs for github
SOCIAL_AUTH_GITHUB_KEY = str(os.getenv('GITHUB_KEY'))
SOCIAL_AUTH_GITHUB_SECRET = str(os.getenv('GITHUB_SECRET'))

# social auth configs for google
SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = str(os.getenv('GOOGLE_KEY'))
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = str(os.getenv('GOOGLE_SECRET'))
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = env.bool("DEBUG", default=True)

ALLOWED_HOSTS = ['*']


INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'store',
    'cart',
    'account',
    'payment',
    'orders', 
    'mptt',
    'core',
    'checkout',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'core.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'store.context_processors.categories',
                'cart.context_processors.cart',
            ],
        },
    },
]

WSGI_APPLICATION = 'core.wsgi.application'


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

import dj_database_url
db_from_env = dj_database_url.config(conn_max_age=600)
DATABASES['default'].update(db_from_env)

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



LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


STATIC_URL = '/static/'

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')
django_heroku.settings(locals())


# Cart session ID
CART_SESSION_ID = 'cart'

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static") 
]





DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
#custom user model
AUTH_USER_MODEL = 'account.Customer'
LOGIN_REDIRECT_URL = '/account/dashboard'
LOGIN_URL = '/account/login/'

#Email Engineering
#EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.mailtrap.io'
EMAIL_HOST_USER = '158095e566a88f'
EMAIL_HOST_PASSWORD = 'f89e692f7d7890'
EMAIL_PORT = 2525
EMAIL_USE_TLS: True

EMAIL_USE_SSL: False


#stripe payment
STRIPE_PUBLISHABLE_KEY = 'pk_test_51L6qnyD62mHbjXxEyhVGuynbgrYRJnZsRS1Pqw1Br8SvO3KfjGLyup2kEOPiQU4UL78VvM9EsGZkyC6HJRXyA3GG00X8wXzo6f'
SECRET_KEY = 'sk_test_51L6qnyD62mHbjXxEVGhEV5XcgzWIa08A4y81wPwOBklFQSAFWOVt7bp3eilsNO7KXxRsYnZNbClSOJTC3JB4tZ0p00L9YaFqnb'
STRIPE_ENDPOINT_SECRET = 'whsec_6ab89491e02131f63c53068da721048a85f3debf43838408acacb8ad84da7f06'

#stripe listen -- forward-to localhost:8000/payment/webhook/

