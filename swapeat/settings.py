"""
Django settings for swapeat project.

Generated by 'django-admin startproject' using Django 5.1.3.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.1/ref/settings/
"""

from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-#t^q$=_^+q00lk6uvi8aon^mazx+_&43-t7x0+pd254e!5h!2#'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'daphne',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'swapfood',
    'channels',
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

ROOT_URLCONF = 'swapeat.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR,"templates")],
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

WSGI_APPLICATION = 'swapeat.wsgi.application'
ASGI_APPLICATION = "swapeat.asgi.application"
CHANNEL_LAYERS = {
   
    "default": {"BACKEND": "channels.layers.InMemoryChannelLayer"},
}




# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

# settings.py


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',  # Use MySQL as the database engine
        'NAME': 'defaultdb',  # Database name
        'USER': 'avnadmin',  # Database user
        'PASSWORD': 'AVNS_BSG5mEedU-2YkT-3tAq',  # Replace with actual password
        'HOST': 'mysql-36fe0488-swapeat.f.aivencloud.com',  # MySQL host
        'PORT': '28836',  # MySQL port
        'OPTIONS': {
            'ssl': {'ssl-mode': 'REQUIRED'},  # Enforce SSL connection
        },
    }
}

# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/

# Static files (CSS, JavaScript, Images)
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# To include the directory where your static files are located:
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
# Media files
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# Redirect after login
LOGIN_URL = '/login/'  # Where users are redirected if not logged in
LOGIN_REDIRECT_URL = '/home/'  # Default page after login
LOGOUT_REDIRECT_URL = '/login/'  # Redirect after logout
# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

ALLOWED_HOSTS = ['grieving-timmie-swapeat-5e816b1d.koyeb.app', 'localhost', '127.0.0.1']

CSRF_TRUSTED_ORIGINS = [
         'https://grieving-timmie-swapeat-5e816b1d.koyeb.app'
]
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'  # Use Gmail or any other email service provider
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'swapeatmail@gmail.com'  # Replace with your email
EMAIL_HOST_PASSWORD = 'anbr opdy syfm alud'  # Replace with your app password
DEFAULT_FROM_EMAIL = 'your_email@gmail.com'




