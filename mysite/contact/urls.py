from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^map', 'contact.views.map'),
    url(r'^mail', 'contact.views.mail'),
    url(r'^$', 'contact.views.main'),
)
