"""
Django settings for NewsPaper project.

Generated by 'django-admin startproject' using Django 4.2.2.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

import os
from dotenv import load_dotenv, find_dotenv
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-6ho^j_q)yuw0l_#@7#u2hjq&er!y)bv8i)%4*z@-21um*sz-w*'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['127.0.0.1']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'news.apps.NewsConfig',


    'accounts',
    'django.contrib.sites',
    'django.contrib.flatpages',
    'sign',
    'protect',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.google',
    'django_apscheduler'
]


ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_UNIQUE_EMAIL = True
ACCOUNT_USERNAME_REQUIRED = True
ACCOUNT_AUTHENTICATION_METHOD = 'email'
ACCOUNT_EMAIL_VERIFICATION = 'mandatory'
ACCOUNT_FORMS = {'signup': 'sign.forms.BasicSignupForm'}

SITE_ID = 1

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware',
]

ROOT_URLCONF = 'NewsPaper.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
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

AUTHENTICATION_BACKENDS = [
               'django.contrib.auth.backends.ModelBackend',
               'allauth.account.auth_backends.AuthenticationBackend',
            ]

WSGI_APPLICATION = 'NewsPaper.wsgi.application'

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.filebased.FileBasedCache',
        'LOCATION': os.path.join(BASE_DIR, 'cache_files'),
    }
}

# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

STATICFILES_DIRS = [
    BASE_DIR / "static"
]

LOGIN_URL = '/accounts/login/'
LOGIN_REDIRECT_URL = '/'



EMAIL_HOST = 'smtp.mail.ru'
EMAIL_PORT = '465'

EMAIL_HOST_USER = 'managernewssk'  # имя пользователя

load_dotenv(find_dotenv())

EMAIL_HOST_PASSWORD = os.getenv('EMAIL_PASSWORD')
EMAIL_USE_SSL = True
SERVER_EMAIL = 'managernewssk@mail.ru'

DEFAULT_FROM_EMAIL = 'managernewssk@mail.ru'



# формат даты, которую будет воспринимать наш задачник(вспоминаем урок по фильтрам)
APSCHEDULER_DATETIME_FORMAT = "N j, Y, f:s a"

# если задача не выполняется за 25 секунд, то она автоматически снимается, можете поставить время побольше, но как правило, это сильно бьёт по производительности сервера
APSCHEDULER_RUN_NOW_TIMEOUT = 25  # Seconds

ADMINS = [("managernewssk", "managernewssk@mail.ru")]

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'formatter_debug': {
            'format': '{asctime}  {levelname}  {message}\n',
            'style': '{',
        },
        'formatter_warning': {
            'format': '{asctime}  {levelname}  {message}  {pathname}\n',
            'style': '{',
        },
        'formatter_error': {
            'format': '{asctime}  {levelname}  {message}  {pathname}  {exc_info}\n',
            'style': '{',
        },
        'formatter_info': {
            'format': '{asctime}  {levelname}  {module}  {message}\n',
            'style': '{',
        },
    },
    'filters': {
            'require_debug_true': {
                '()': 'django.utils.log.RequireDebugTrue',
            },
            'require_debug_false': {
                '()': 'django.utils.log.RequireDebugFalse',
            },
    },
    'handlers': {
        'console_debug': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'formatter_debug',
            'filters': ['require_debug_true'],
        },
        'console_warning': {
            'level': 'WARNING',
            'class': 'logging.StreamHandler',
            'formatter': 'formatter_warning',
            'filters': ['require_debug_true'],
        },
        'console_error': {
            'level': 'ERROR',
            'class': 'logging.StreamHandler',
            'formatter': 'formatter_error',
            'filters': ['require_debug_true'],
        },
        'file_info': {
            'level': 'INFO',
            'class': 'logging.FileHandler',
            'filename': 'general.log',
            'formatter': 'formatter_info',
            'filters': ['require_debug_false'],
        },
        'file_error': {
            'level': 'ERROR',
            'class': 'logging.FileHandler',
            'filename': 'errors.log',
            'formatter': 'formatter_error',
        },
        'file_security': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': 'security.log',
            'formatter': 'formatter_info',
        },
        'mail_admins': {
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler',
            'formatter': 'formatter_warning',
            'filters': ['require_debug_false'],
        },
    },

        'loggers': {
        'django': {
            'handlers': ['console_debug', 'console_warning', 'console_error', 'file_info'],
            'level': 'DEBUG',
            'propagate': True,
        },
        'django.request': {
            'handlers': ['file_error', 'mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
        'django.server': {
            'handlers': ['file_error', 'mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
        'django.template': {
            'handlers': ['file_error'],
            'level': 'ERROR',
            'propagate': True,
        },
        'django.db_backends': {
            'handlers': ['file_error'],
            'level': 'ERROR',
            'propagate': True,
        },
        'django.security': {
            'handlers': ['file_security'],
            'level': 'DEBUG',
            'propagate': True,
        },
        'error': {
            'handlers': ['file_error'],
            'level': 'ERROR',
            'propagate': True,
        },
    },
}

