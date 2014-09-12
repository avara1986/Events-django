from django.conf.urls import patterns, url, include

from common.api import CityList, StateList, CountryList

urlpatterns = patterns('',
    url(r'^cities/(?P<state>[0-9a-zA-Z_-]+)$', CityList.as_view(), name='city-list'),
    url(r'^states/(?P<country>[0-9a-zA-Z_-]+)$', StateList.as_view(), name='state-list'),
    url(r'^countries/$', CountryList.as_view(), name='country-list'),
)
