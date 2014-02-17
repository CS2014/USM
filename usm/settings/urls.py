from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'usm.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
		url(r'^main/', include('main.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounting/', include('accounting.urls')),
)
