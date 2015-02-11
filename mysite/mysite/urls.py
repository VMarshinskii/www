from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^catalog/', include('catalog.urls')),
    url(r'^contact/', include('contact.urls')),
    url(r'^tinymce/', include('tinymce.urls')),
    url(r'^redactor/', include('redactor.urls')),
    url(r'^clients/', include('clients.urls')),
    url(r'^orders/', include('orders.urls')),
    url(r'^admin/', include('settings.urls')),
    url(r'^$', 'catalog.views.home'),
    url(r'', include('pages.urls')),
)
