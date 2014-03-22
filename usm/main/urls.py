from django.conf.urls import patterns, include ,url

from main import views

urlpatterns = patterns('main.views',
	url(r'^main/create_society/', views.create_society),
	url(r'^signup/$', views.signup),
	url(r'^logout/$', views.logout_view),
	url(r'^$', views.index),
	url(r'^create_society/', views.create_society),
	url(r'^(?P<slug>[\w-]+)/$', views.society_page),
	url(r'^(?P<slug>[\w-]+)/book-keeping$', views.society_book_keeping),
)