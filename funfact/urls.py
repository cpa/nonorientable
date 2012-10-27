from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

from django.contrib.staticfiles.urls import staticfiles_urlpatterns

# STATICFILES_DIRS = ("/Users/cpa/prog/funfact/")
STATIC_URLS = 'static/'

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'funfact.views.home', name='home'),
    # url(r'^funfact/', include('funfact.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'funlog.views.index', name='index'),
)

# ... the rest of your URLconf goes here ...

urlpatterns += staticfiles_urlpatterns()
