from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # REST - Modelo y Controlador del proyecto
    url(r'^api/', include('events.api.urls')),
    # REST - Modelo y Controlador del proyecto
    url(r'^api/common/', include('common.urls')),
    # grappelli URLS
    (r'^grappelli/', include('grappelli.urls')), 
    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    # FE - Vista del Proyecto
    url(r'^', include('landing.urls')),
)
