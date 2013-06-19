from django.conf.urls.defaults import *
from django.contrib import admin
from django.conf import settings

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('fle_site.views',
	url(r'^$', 'landingpage', name='landingpage'),
	# url(r'^about/$', 'about', name='about'),
	# url(r'^getinvolved/$', 'involved', name='involved'),
    url(r'^map/$', 'map', name='map'),
)

urlpatterns += patterns('',
    url(r'^admin/', include(admin.site.urls)),
)

if settings.DEBUG:
    urlpatterns = patterns('',
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),
    url(r'', include('django.contrib.staticfiles.urls')),
) + urlpatterns
