from django.conf.urls import patterns, url

urlpatterns = patterns(
    'api.views',
    url(r'^users/$', 'user_list', name='user_list'),
    url(r'^users/(?P<pk>[0-9]+)$', 'user_detail', name='user_detail'),
    url(r'^users/preferences/(?P<id>[0-9]+)$', 'user_preferences', name='user_preferences'),
    url(r'^users/photos/user/(?P<id>[0-9]+)$', 'user_photos', name='user_photos'),
    url(r'^users/relations/(?P<id>[0-9]+)$', 'user_relations', name='user_relations'),
)
