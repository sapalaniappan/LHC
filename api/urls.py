from django.conf.urls import patterns, url
from api.views import UserView,UserEmail,ArticleList

urlpatterns = patterns(
    'api.views',
    url(r'^users/$', 'user_list', name='user_list'),
    url(r'^users/email/(?P<email>[\w.%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,4})$', 'user_detail_by_email', name='user_detail_by_email'),
    url(r'^users/detail/email/(?P<email>[\w.%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,4})$', 'user_full_detail_by_email', name='user_full_detail_by_email'),
    url(r'^users/(?P<pk>[0-9]+)$', 'user_detail', name='user_detail'),
    url(r'^users/preferences/(?P<id>[0-9]+)$', 'user_preferences', name='user_preferences'),
    url(r'^users/photos/user/(?P<id>[0-9]+)$', 'user_photos', name='user_photos'),
    url(r'^users/chats/user/(?P<id>[0-9]+)$', 'user_chats', name='user_chats'),
    url(r'^users/properties/user/(?P<userid>[0-9]+)$', 'user_properties', name='user_properties'),
    url(r'^users/relations/user/(?P<id>[0-9]+)$', 'user_relations', name='user_relations'),
    url(r'^users/events/user/(?P<id>[0-9]+)$', 'user_events', name='user_events'),
    url(r'^users/events/$', 'events', name='events'),
    url(r'^events/(?P<id>[0-9]+)$', 'events_by_id', name='events_by_id'),
    url(r'^user/(?P<id>[0-9]+)$', UserView.as_view(), name='user-view'),
    url(r'^user/email/(?P<email>[\w.%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,4})$', UserEmail.as_view(), name='user-email'),
    url(r'^photos/$', ArticleList.as_view(),name='article-list'),
)
