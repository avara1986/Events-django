from django.conf.urls import patterns, url, include

from .api import EventList
from .api import AttendeeList


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
'''
user_urls = patterns('',
    url(r'^/(?P<username>[0-9a-zA-Z_-]+)/posts$', UserPostList.as_view(), name='userpost-list'),
    url(r'^/(?P<username>[0-9a-zA-Z_-]+)$', UserDetail.as_view(), name='user-detail'),
    url(r'^$', UserList.as_view(), name='user-list')
)

post_urls = patterns('',
    url(r'^/(?P<pk>\d+)/photos$', PostPhotoList.as_view(), name='postphoto-list'),
    url(r'^/(?P<pk>\d+)$', PostDetail.as_view(), name='post-detail'),
    url(r'^$', PostList.as_view(), name='post-list')
)

photo_urls = patterns('',
    url(r'^/(?P<pk>\d+)$', PhotoDetail.as_view(), name='photo-detail'),
    url(r'^$', PhotoList.as_view(), name='photo-list')
)

urlpatterns = patterns('',
    url(r'^users', include(user_urls)),
    url(r'^posts', include(post_urls)),
    url(r'^photos', include(photo_urls)),
)
'''
