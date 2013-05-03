from django.conf.urls.defaults import *
from django.contrib import admin
from django.conf import settings

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
	url(r'^$', 'fle_site.views.landingpage', name='landingpage'),
	url(r'^about/$', 'fle_site.views.about', name='about'),
	url(r'^getinvolved/$', 'fle_site.views.involved', name='involved'),
    url(r'^d3/$', 'fle_site.views.d3', name='d3'),
    url(r'^blog/$', 'fle_site.views.blog', name='blog'),
    # Examples:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include('cms.urls')),



 
)

if settings.DEBUG:
    urlpatterns = patterns('',
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),
    url(r'', include('django.contrib.staticfiles.urls')),
) + urlpatterns
