from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
	url(r'^$', 'fle_site.views.landingpage', name='landingpage'),
	url(r'^about/$', 'fle_site.views.about', name='about'),
	url(r'^getinvolved/$', 'fle_site.views.involved', name='involved'),
    url(r'^d3/$', 'fle_site.views.d3', name='d3'),


    # Examples:
    # url(r'^$', 'fle_site.views.home', name='home'),
    # url(r'^fle_site/', include('fle_site.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
