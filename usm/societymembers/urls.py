from django.conf.urls import patterns, url

from societymembers import views

urlpatterns = patterns('societymembers.views',
    url(r'^$', views.member_index, name='member_index'),
    url(r'^new/$', views.member_add, name= 'member_add'),
    url(r'^(?P<member_id>\d+)/delete/$', views.member_delete, name='member_delete'),
    url(r'^denied/$', views.member_denied, name='member_denied'),
    url(r'^(?P<member_id>\d+)/$', views.member_detail, name='member_detail'),
    url(r'^(?P<member_id>\d+)/edit/$', views.member_edit, name='member_edit'),
)