import django.core.handlers.wsgi
import os
# specify the name of your settings module
os.environ['DJANGO_SETTINGS_MODULE'] = 'events.settings'


application = django.core.handlers.wsgi.WSGIHandler()