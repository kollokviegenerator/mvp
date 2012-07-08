from django.conf.urls import patterns, include, url
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    url( r'^admin/',                include(admin.site.urls)),
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url( r'^$',                     'mvp.views.main' ),
    url( r'^add/$',                 'mvp.views.add' ),
    url( r'^display/$',             'mvp.views.display' ),
    url( r'^flush/$',               'mvp.views.flush' ),
    # testing (throw into own app)
    url( r'^test/students/$',               'mvp.views.display_students' ),
    url( r'^test/students/populate/$',      'mvp.views.populate_students' ),
    url( r'^test/wishes/$',                 'mvp.views.display_wishes' ),
    url( r'^test/wishes/populate/$',        'mvp.views.populate_wishes' ),
    url( r'^test/wishes/flush/$',           'mvp.views.flush_wishes' ),
    url( r'^test/intrude/([a-z]{1,10})',    'mvp.views.intrude' ),
    # other project applications
    url( r'^match/',                include('match.urls')),

    url(r'^groups/',                  'mvp.views.group'),
)
