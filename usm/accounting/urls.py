from django.conf.urls import patterns, url

from accounting import views

urlpatterns = patterns('accounting.views',

		#/accounting/
    url(r'^$', views.index),
    url(r'^transactions/', views.transaction_index),
)