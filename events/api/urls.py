from django.conf.urls import patterns, url, include

from events.api.api import EventList, AttendeeList


event_urls = patterns('',
    #url(r'^/(?P<username>[0-9a-zA-Z_-]+)/posts$', UserPostList.as_view(), name='userpost-list'),
    #url(r'^/(?P<username>[0-9a-zA-Z_-]+)$', UserDetail.as_view(), name='user-detail'),
    url(r'^/$', EventList.as_view(), name='event-list')
)

attendee_urls = patterns('',
    #url(r'^/(?P<username>[0-9a-zA-Z_-]+)/posts$', UserPostList.as_view(), name='userpost-list'),
    url(r'^/$',  AttendeeList.as_view(), name='attendee-list'),
    #url(r'^/(?P<pk>\d+)$', AttendeeDetail.as_view(), name='attendee-detail'),
)

urlpatterns = patterns('',
    url(r'^events', include(event_urls)),
    url(r'^attendees', include(attendee_urls)),
)
