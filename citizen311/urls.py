from django.conf.urls import patterns, include, url
from django.contrib.auth.views import login

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('app.views',
	url(r'^$', 'home.main', name='home'),
    url(r'^reports$', 'myapp.reports', name='reports'),
    url(r'^about$', 'myapp.about', name='about'),
    url(r'^submit$', 'myapp.submit', name='submit'),
    url(r'^signup$', 'myapp.signup', name='signup'),
    url(r'^lookup/(?P<id>\d+)$', 'myapp.lookup', name='lookup'),
    url(r'^login$', 'myapp.login', name='login'),
#    url(r'^lookup$', 'myapp.lookup', name='lookup'),
    url(r'^enter-comments$', 'myapp.comments', name='comments'),
    url(r'^logout$', 'myapp.logout_views', name='logout_views')

    # Examples:
    # url(r'^$', 'citizen311.views.home', name='home'),
    # url(r'^citizen311/', include('citizen311.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
