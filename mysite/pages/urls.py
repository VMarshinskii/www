from django.conf.urls import patterns, include, url


urlpatterns = patterns('',
    url(r'^(?P<section_url>[\-\w]+)/$', 'pages.views.section'),
    url(r'^(?P<section_url>[\-\w]+)/(?P<page_url>[\-\w]+)/$', 'pages.views.page'),
)
