from django.conf.urls import patterns, include ,url

from main import views

urlpatterns = patterns('main.views',
	url(r'^main/create_society/', views.create_society),
	url(r'^signup/$', views.signup),
	url(r'^logout/$', views.logout_view),
	url(r'^request_membership/$', views.request_membership),
	url(r'^create_society/$', views.create_society),
	url(r'^$', views.homepage),
	url(r'^(?P<slug>[\w-]+)/$', views.dash_board),
	url(r'^(?P<slug>[\w-]+)/member_requests/$', views.member_requests),
	url(r'^(?P<slug>[\w-]+)/member_requests/accept/(?P<user_index>[\w-]+)/$', views.accept_join_request),
	url(r'^(?P<slug>[\w-]+)/member_requests/reject/(?P<user_index>[\w-]+)/$', views.reject_join_request),
)