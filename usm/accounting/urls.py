from django.conf.urls import patterns, url

from accounting import views

urlpatterns = patterns('accounting.views',    
    #Edits
    url(r'transaction_categories/(?P<id>\d+)/edit$', views.transaction_category_edit),
    url(r'transactions/(?P<id>\d+)/edit$', views.transaction_edit),
    url(r'grants/(?P<id>\d+)/edit$', views.grant_edit),
)