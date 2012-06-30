from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url( r'^admin/',                include(admin.site.urls)),
    url( r'^intrude/([a-z]{1,10})', 'mvp.views.intrude' ),
    url( r'^$',                     'mvp.views.main' ),
    url( r'^add/$',                 'mvp.views.add' ),
    url( r'^display/$',             'mvp.views.display' ),
    url( r'^flush/$',               'mvp.views.flush' ),
    # wish testing
    url( r'^test/wishes/populate$', 'mvp.views.test_wishes' ),
    url( r'^test/wishes/display$',  'mvp.views.display_wishes' ),
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
)
