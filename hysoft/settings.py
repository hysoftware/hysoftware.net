"""
Django settings for hysoft project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
import random
from datetime import timedelta

BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False
if os.environ.get("DEBUG", "False").lower() == "true":
    DEBUG = True

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = None

TEMPLATE_DEBUG = DEBUG

ALLOWED_HOSTS = [
    "hysoftware.net",
    "www.hysoftware.net",
    "localhost"
]
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
        },
    },
    'loggers': {
        'django.request': {
            'handlers': ['console'],
            'level': 'ERROR',
            'propagate': True,
        },
    },
}

if DEBUG:
    SECRET_KEY = ("").join(
        [
            random.choice(
                "abcdefghijklmnopqrstuvwxyz"
                "ABCDEVGHIJKLMNOPQRSTUVWXYZ"
                "0123456789"
                "`~!@#$%^&*()-_=+[{]}\\|\"';:/?.>,<"
            )
        ]
    )
    ALLOWED_HOSTS = ["*"]
else:
    SECRET_KEY = os.environ["SECRET"]


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.webdesign',

    'about',
    'contact',
    'home'
)

MIDDLEWARE_CLASSES = (
    'django.middleware.gzip.GZipMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'dj_ajax_redirect.middleware.AjaxRedirectionMiddleware'
)

DISABLE_REDIRECT = [
    r"^manager"
]

ROOT_URLCONF = 'hysoft.urls'

WSGI_APPLICATION = 'hysoft.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': ('django.db.backends.sqlite3'
                   if DEBUG else
                   'django.db.backends.postgresql_psycopg2'),
        'NAME': (os.path.join(BASE_DIR, 'hysoft.db')
                 if DEBUG else os.environ.get("db_name", "hysoft")),
        'USER': os.environ.get("db_user"),
        'PASSWORD': os.environ.get("db_pw"),
        'HOST': os.environ.get("db_host", "127.0.0.1")
    }
}

# Templates
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            # insert your TEMPLATE_DIRS here
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                # Insert your TEMPLATE_CONTEXT_PROCESSORS here or use this
                # list if you haven't customized them:
                'django.contrib.auth.context_processors.auth',
                'django.template.context_processors.debug',
                'django.template.context_processors.i18n',
                'django.template.context_processors.media',
                'django.template.context_processors.static',
                'django.template.context_processors.tz',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.environ.get("STATIC_ROOT", "staticfiles")
STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticFilesStorage'

# Session settings
SESSION_COOKIE_SECURE = False
SESSION_ENGINE = "django.contrib.sessions.backends.cached_db"
SESSION_EXPIRE_AT_BROWSER_CLOSE = True
SESSION_COOKIE_SECUR = os.environ.get("SSL_MODE", False)
CSRF_COOKIE_SECURE = SESSION_COOKIE_SECUR


# Email settings
EMAIL_BACKEND = None

if DEBUG:
    EMAIL_BACKEND = 'django.core.mail.backends.locmem.EmailBackend'
else:
    EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

EMAIL_HOST = os.environ.get("EMAIL_HOST", "localhost")
EMAIL_HOST_PASSWORD = os.environ.get("EMAIL_PW", "")
EMAIL_HOST_USER = os.environ.get("EMAIL_USER", "")
EMAIL_PORT = int(os.environ.get("EMAIL_PORT", "25"))

# CSRF settings
CSRF_COOKIE_NAME = "XSRF-TOKEN"
CONTACT_VIRIFICATION_EXPIRES = timedelta(hours=2)
