"""
Django settings for backend project.

Generated by 'django-admin startproject' using Django 3.2.8.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""
import os
from pathlib import Path
from dotenv import dotenv_values
import rest_framework


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-8#p9v==cppe--$%0ijs@8gzy$0*i_025^h(9v*_u7%e8%!3nas'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    
    # third party apps
    'rest_framework',
    'rest_framework.authtoken',
    'corsheaders',
    'debug_toolbar',

    # local apps
    'api',
    'tips', #blog


    # 'django_filters',
    # 'taggit',
    'ckeditor',
    'ckeditor_uploader',
    # 'crispy_forms',
    # 'blog.apps.BlogConfig',
]

MIDDLEWARE = [
    "corsheaders.middleware.CorsMiddleware",
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware',
]

ROOT_URLCONF = 'backend.urls'

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

WSGI_APPLICATION = 'backend.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

config = dotenv_values(".env")

DATABASES = {
    'default': {
        'ENGINE': config['DB_ENGINE'],
        'NAME': config['DB_NAME'],
        'USER': config['DB_USER'],
        'PASSWORD': config['DB_PASS'],
        'HOST': config['DB_HOST'],
        'PORT': config['DB_PORT'],
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

CORS_ORIGIN_ALLOW_ALL = False
CORS_ORIGIN_WHITELIST = ("http://localhost:8000",)

# CKEditor Settings
CKEDITOR_UPLOAD_PATH = 'uploads/'
CKEDITOR_IMAGE_BACKEND = "pillow"

CKEDITOR_CONFIGS = {
    'default': {
        # 'toolbar': 'full',
        'width': 'auto',
        'height': 50
        # 'extraPlugins': ','.join([
        #     'codesnippet',
        #     'youtube'
        # ]),
    },
}

INTERNAL_IPS = [
    # ...
    '127.0.0.1',
    # ...
]

# Account Settings
LOGIN_URL = '/account/login/'
LOGIN_REDIRECT_URL = '/author/dashboard/'
LOGOUT_REDIRECT_URL = '/account/logout/'

# Email Settings (Development)
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# Email Settings (Production)
EMAIL_BACKEND = ''
EMAIL_HOST = ''
EMAIL_HOST_USER = ''
EMAIL_HOST_PASSWORD = ""
EMAIL_PORT = 587
EMAIL_USE_TLS = True

STATICFILES_DIRS = [ 
    # BASE_DIR / "static",
    # os.path.join(BASE_DIR, "blog/static"),
]
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_FINDERS = [
    "django.contrib.staticfiles.finders.FileSystemFinder",
    "django.contrib.staticfiles.finders.AppDirectoriesFinder",
]

# Media files (User uploaded images)
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',
    ]
}

CORS_ALLOWED_ORIGINS = [
    "http://localhost:3000",                                
]