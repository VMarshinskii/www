from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', 'catalog.views.catalog'),
    url(r'^(?P<categ_name>[\-\w]+)/(?P<product_id>\d+)/$', 'catalog.views.product'),
    url(r'^(?P<categ_name>[\-\w]+)/$', 'catalog.views.category'),
    url(r'^ajax/filter/', 'catalog.views.ajax_filter'),
)
