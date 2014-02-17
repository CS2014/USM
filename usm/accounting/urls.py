from django.conf.urls import patterns, url

from accounting import views

urlpatterns = patterns('accounting.views',

	#indexs
    url(r'^$', 'index'),
    url(r'^accounts/$', views.account_index),
   	url(r'^transaction_categories/$', views.transaction_category_index),
    url(r'^transaction_methods/$', views.transaction_method_index),
    url(r'^transactions/$', views.transaction_index),
    url(r'^bills/$', views.bill_index),
    url(r'^invoices/$', views.invoice_index),
	url(r'^grants/$', views.grant_index),

    #Creates
    url(r'^accounts/new', views.account_new),
   	url(r'^transaction_categories/new', views.transaction_category_new),
    url(r'^transaction_methods/new', views.transaction_method_new),
    url(r'^transactions/new', views.transaction_new),
    url(r'^bills/new', views.bill_new),
    url(r'^invoices/new', views.invoice_new),
	url(r'^grants/new', views.grant_new),

    #Details
    url(r'accounts/(?P<id>\d+)/$', views.account_detail),   
    url(r'transaction_categories/(?P<id>\d+)/$', views.transaction_category_detail),
    url(r'transaction_methods/(?P<id>\d+)/$', views.transaction_method_detail),
    url(r'transactions/(?P<id>\d+)/$', views.transaction_detail),
    url(r'bills/(?P<id>\d+)/$', views.bill_detail),
    url(r'invoices/(?P<id>\d+)/$', views.invoice_detail),
    url(r'grants/(?P<id>\d+)/$', views.grant_detail),

    #Edits
    url(r'accounts/(?P<id>\d+)/edit$', views.account_edit),
    url(r'transaction_categories/(?P<id>\d+)/edit$', views.transaction_category_edit),
    url(r'transaction_methods/(?P<id>\d+)/edit$', views.transaction_method_edit),
    url(r'transactions/(?P<id>\d+)/edit$', views.transaction_edit),
    url(r'bills/(?P<id>\d+)/edit$', views.bill_edit),
    url(r'invoices/(?P<id>\d+)/edit$', views.invoice_edit),
    url(r'grants/(?P<id>\d+)/edit$', views.grant_edit),
)