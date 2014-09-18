#encoding: utf-8
"""
For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
# Project dir carga hasta nombre-proyecto/nombre-proyecto (a la altura de
# url.py y settings.py)
PROJECT_DIR = os.path.abspath(os.path.dirname(__file__))

# base dir carga hasta nombre-proyecto/ (a la altura de manage.py
BASE_DIR = os.path.dirname(os.path.dirname(__file__)) + os.sep

DEBUG = TEMPLATE_DEBUG = True

ADMINS = (
          ('Alberto', 'a.vara.1986@gmail.com'),
          )
MANAGERS = ADMINS
# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '=(q1=cih&&p6dz5+)h=o@-fom%7__juz!%1leru&@8*s7!lmg-'


# Application definition
INSTALLED_APPS = (
    'grappelli',
    'import_export',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'django.contrib.admindocs',
    'django_extensions',
    'south',
    'rest_framework',
    'corsheaders',
    'dynamic_form',
    'common',
    'landing',
    'events.api',
)

if 'HEROKU_POSTGRESQL_OLIVE_URL' in os.environ:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': 'ddsf0049qm097c',
            'USER': os.environ.get('HEROKU_EVENTS_USER'),
            'PASSWORD': os.environ.get('HEROKU_EVENTS_PASSWORD'),
            'HOST': os.environ.get('HEROKU_EVENTS_HOST'),
            'PORT': '5432',
        }
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        }
    }
    '''
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': '',
            'USER':  '',
            'PASSWORD': '',
            'HOST': 'localhost',
            'PORT': '3306',
        }
    }
    '''

# Honor the 'X-Forwarded-Proto' header for request.is_secure()
#SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# Allow all host headers
ALLOWED_HOSTS = ['*']


MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'events.urls'

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'events.wsgi.application'

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/
SITE_ID = 1

LANGUAGE_CODE = 'es-ES'

TIME_ZONE = 'Europe/Madrid'

#formato espa�ol
DATE_FORMAT = 'j/m/Y'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/home/media/media.lawrence.com/media/"
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/var/www/example.com/media/"
MEDIA_URL = '/media/'

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/
STATIC_URL = '/static/'

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://example.com/media/", "http://media.example.com/"
# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/var/www/example.com/static/"
#STATIC_ROOT = os.path.join(BASE_DIR,'static')
# Additional locations of static files
STATIC_ROOT = os.path.join(BASE_DIR, 'static')


STATICFILES_DIRS = (
    os.path.join(PROJECT_DIR, 'static'),
    os.path.join(PROJECT_DIR, 'assets'),
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)


# Additional locations of static files
TEMPLATE_DIRS = (
    os.path.join(PROJECT_DIR, 'templates'),
)

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    'django.core.context_processors.tz',
    'django.core.context_processors.request',
    'django.contrib.messages.context_processors.messages',
)

#MAIL
#cualuiqer servidor de correo (informaci�n aportado por el ISP)
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587   # puerto 465
EMAIL_HOST_USER = 'no-reply@gmail.com'
EMAIL_HOST_PASSWORD = '***'
EMAIL_USE_TLS = True
DEFAULT_FROM_EMAIL = 'no-reply@gobalo.es'

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

FILE_CHARSET = 'utf-8'

SESSION_SERIALIZER = 'django.contrib.sessions.serializers.JSONSerializer'

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}
#REST FRAMEWORK
REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': (
        #'rest_framework.permissions.IsAuthenticated',
        'rest_framework.permissions.AllowAny',
    ),
}
#GRAPELLI ADMIN STYLES
GRAPPELLI_ADMIN_TITLE = "Events in django"

#CORS TODO: remove ALLOW ALL
CORS_ORIGIN_ALLOW_ALL = True

#DYNAMIC FORM
DYNAMIC_FORM_MODEL_IMPORT = 'events'
DYNAMIC_FORM_QUESTION_FK_MODEL = 'Event'
DYNAMIC_FORM_ANSWER_FK_MODEL = 'Attendee'
