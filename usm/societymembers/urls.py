from django.conf.urls import patterns, url

from societymembers import views

urlpatterns = patterns('societymembers.views',
    
    url(r'^$', views.member_index, name='member_index'),
    url(r'^delete/$', views.member_delete, name='member_delete'),
    url(r'^(?P<member_id>\d+)/$', views.member_detail, name='member_detail'),
    url(r'^(?P<member_id>\d+)/edit/$', views.member_edit, name='member_edit'),
)