from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('app.views',
	url(r'^$', 'home.main', name='home'),
    url(r'^reports$', 'app.reports', name='reports'),
    url(r'^about$', 'app.about', name='about'),
    url(r'^submit$', 'app.submit', name='submit'),
    url(r'^signup$', 'app.signup', name='signup'),


    # Examples:
    # url(r'^$', 'citizen311.views.home', name='home'),
    # url(r'^citizen311/', include('citizen311.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
