from django.conf.urls import patterns, url

from accounting import views

urlpatterns = patterns('accounting.views',

	#indexs
    url(r'^$', views.index),
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

)