from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/',     include(admin.site.urls)),
    url(r'^$',          'mvp.views.main' ),
    url(r'^add/$',      'mvp.views.add' ),
    url(r'^display/$',  'mvp.views.display' ),
    url(r'^flush/$',    'mvp.views.flush' ),

    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
)
