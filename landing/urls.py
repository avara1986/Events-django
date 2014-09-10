from django.conf.urls import patterns, include, url

urlpatterns = patterns('landing.views',
    # FE - Vista del Proyecto
    url(r'^$', 'index', name='index_landing'),
    url(r'^confirm/(?P<idattendee>\d+)/$', 'confirm', name='confirm'),
    url(r'^invitation/(?P<idattendee>\d+)/$', 'invitation', name='invitation'),
)
