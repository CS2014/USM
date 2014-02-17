from django.conf.urls import patterns, include ,url

from main import views

urlpatterns = patterns('main.views',
	url(r'^main/create_society/', views.create_society),
	url(r'^$', views.index),
)