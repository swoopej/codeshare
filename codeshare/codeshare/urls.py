from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'codeshare.views.home', name='home'),
    # url(r'^codeshare/', include('codeshare.foo.urls')),
    
    # Uncomment the admin/doc line below to enable admin documentation:
    (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    (r'^admin/', include(admin.site.urls)),
    (r'^snippets/', include('cab.urls.snippets')),
    (r'^languages/', include('cab.urls.languages')),
    (r'^popular/', include('cab.urls.popular')),
)
