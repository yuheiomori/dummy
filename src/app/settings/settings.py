# coding=utf-8
"""
Django settings for sandbox project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '%y=pyskhqjbzg4*q*wm!**6j^f-rsn&uyg39a7d$)n0fzqy&&j'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = ['namahage.link']

# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'app.users',
    'django_bouncy'
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'app.urls'

WSGI_APPLICATION = 'app.wsgi.application'

# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'ja-jp'

TIME_ZONE = 'Asia/Tokyo'

USE_I18N = True

USE_L10N = True

USE_TZ = False

#####################
# ディレクトリ基準
#####################
REPOSITORY_ROOT = os.path.abspath(os.path.join(
    os.path.dirname(__file__),  # settings
    "..",  # app (django project dir)
    "..",  # src (source root)
    "..",  # vocal-myu (repository root)
))
SRC_DIR = os.path.join(REPOSITORY_ROOT, "src")
APP_DIR = os.path.join(SRC_DIR, "app")


TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(SRC_DIR, 'templates')],
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

STATICFILES_DIRS = (
    os.path.join(REPOSITORY_ROOT, 'static'),
)

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = '/static/'

LOG_DIR = '/var/log/sandbox'
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'formatters': {
        "verbose": {
            "format": "[in %(pathname)s:%(lineno)d] %(asctime)s %(levelname)s %(module)s %(process)d %(thread)d: %(message)s",
            'datefmt': "%Y-%m-%d %H:%M:%S",
        },
    },
    'handlers': {
        'app': {
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': os.path.join(LOG_DIR, 'app.log'),
            'maxBytes': 1024 * 1024 * 5,  # 5 MB
            'formatter': 'verbose'
        },
    },
    'loggers': {
        'django.request': {
            'handlers': ['app'],
            'level': 'DEBUG',
            'propagate': True
        },
        'app': {
            'handlers': ['app'],
            'level': 'DEBUG',
            'propagate': True
        },
    }
}

BOUNCY_TOPIC_ARN = ['arn:aws:sns:us-west-2:748231602871:bounce-y0m0r1-link',
                    'arn:aws:sns:us-west-2:748231602871:complaients-y0m0r1-link']
