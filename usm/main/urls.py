from django.conf.urls import patterns, include ,url

from main import views as main_views
from accounting import views as accounting_views

urlpatterns = patterns('main.views',
	url(r'^main/create_society/', main_views.create_society),
	url(r'^register/$', main_views.signup),
	url(r'^login/$', main_views.user_login),
	url(r'^logout/$', main_views.logout_view),
	url(r'^request_membership/$', main_views.request_membership),
	url(r'^create_society/$', main_views.create_society),
	url(r'^$', main_views.homepage),
	url(r'^(?P<slug>[\w-]+)/$', main_views.dash_board),
	url(r'^(?P<slug>[\w-]+)/transactions/$', accounting_views.society_book_keeping),	
	url(r'^(?P<slug>[\w-]+)/transactions/create/$', accounting_views.society_book_keeping),	
	url(r'^(?P<slug>[\w-]+)/transactions/delete/(?P<id>\d+)$', accounting_views.transaction_delete),	
	url(r'^(?P<slug>[\w-]+)/member_requests/$', main_views.member_requests),
	url(r'^(?P<slug>[\w-]+)/member_requests/accept/(?P<user_index>[\w-]+)/$', main_views.accept_join_request),
	url(r'^(?P<slug>[\w-]+)/member_requests/reject/(?P<user_index>[\w-]+)/$', main_views.reject_join_request),
)