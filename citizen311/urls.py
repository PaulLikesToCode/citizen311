from django.conf.urls import patterns, include, url
from django.contrib.auth.views import login
from tastypie.api import Api
from app.api.resources import Complaints, Comments

v1_api = Api(api_name='v1')
v1_api.register(Complaints())
v1_api.register(Comments())

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('app.views',
	url(r'^$', 'home.main', name='home'),
    url(r'^reports$', 'myapp.reports', name='reports'),
    url(r'^about$', 'myapp.about', name='about'),
    url(r'^submit$', 'myapp.submit', name='submit'),
    url(r'^signup$', 'myapp.signup', name='signup'),
#    url(r'^lookup/(?P<id>\d+)$', 'myapp.lookup', name='lookup'),
    url(r'^login$', 'myapp.login', name='login'),
    url(r'^lookup$', 'myapp.lookup', name='lookup'),
    url(r'^enter-comments$', 'myapp.comments', name='comments'),
    url(r'logout$', 'myapp.logout_views', name='logout_views'),
    url(r'^markers-info', 'myapp.markers_info', name='markers_info'),
    url(r'^api/', include(v1_api.urls)),
    url(r'^lookup/(?P<id>\d+)$', 'myapp.lookup_report', name='lookup_report')
    # Examples:
    # url(r'^$', 'citizen311.views.home', name='home'),
    # url(r'^citizen311/', include('citizen311.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
