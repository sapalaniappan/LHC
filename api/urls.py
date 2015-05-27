from django.conf.urls import patterns, url

urlpatterns = patterns(
    'api.views',
    url(r'^tasks/$', 'user_list', name='user_list'),
    url(r'^tasks/(?P<pk>[0-9]+)$', 'user_detail', name='user_detail'),
)
