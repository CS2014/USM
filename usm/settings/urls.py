from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounting/', include('accounting.urls')),
    url(r'^(?P<slug>[\w-]+)/members/', include('societymembers.urls', namespace="societymembers")),
    url(r'^(?P<slug>[\w-]+)/messaging/', include('communications.urls', namespace="communications")),
    url(r'^', include('main.urls', namespace="main")),
)
