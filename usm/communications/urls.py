from django.conf.urls import patterns, url

from communications import views

urlpatterns = patterns('societymembers.views',
    url(r'^sms/', views.send_sms, name='send_sms'),
    url(r'^email/', views.send_email, name='send_email'),
)