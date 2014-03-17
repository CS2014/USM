from django.conf.urls import patterns, url

from societymembers import views

urlpatterns = patterns('societymembers.views',
    
    url(r'^$', views.member_index, name='member_index'),
    url(r'^delete/$', views.member_delete, name='member_delete'),
)