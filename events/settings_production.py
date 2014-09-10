from settings import *

DEBUG = TEMPLATE_DEBUG = False

ALLOWED_HOSTS = ['localhost',
                 'test-django-cloud-sql-1234.appspot.com']

EMAIL_HOST_PASSWORD = '***'

import appengine_toolkit
# Running on production App Engine, so use a Google Cloud SQL database.
DATABASES = {
    'default': appengine_toolkit.config(),
}

DEFAULT_FILE_STORAGE = 'appengine_toolkit.storage.GoogleCloudStorage'
STATICFILE_STORAGE = 'appengine_toolkit.storage.GoogleCloudStorage'
