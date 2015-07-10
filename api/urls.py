from django.conf.urls import patterns, url

urlpatterns = patterns(
    'api.views',
    url(r'^users/$', 'user_list', name='user_list'),
    url(r'^users/email/(?P<email>[\w.%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,4})$', 'user_detail_by_email', name='user_detail_by_email'),
    url(r'^users/(?P<pk>[0-9]+)$', 'user_detail', name='user_detail'),
    url(r'^users/preferences/(?P<id>[0-9]+)$', 'user_preferences', name='user_preferences'),
    url(r'^users/photos/user/(?P<id>[0-9]+)$', 'user_photos', name='user_photos'),
    url(r'^users/chats/user/(?P<id>[0-9]+)$', 'user_chats', name='user_chats'),
    url(r'^users/properties/user/(?P<userid>[0-9]+)$', 'user_properties', name='user_properties'),
    url(r'^users/relations/(?P<id>[0-9]+)$', 'user_relations', name='user_relations'),
)
