from django.conf.urls import patterns, url

from accounting import views

urlpatterns = patterns('',

		#/accounting/
    url(r'^$', views.index, name='index')
)