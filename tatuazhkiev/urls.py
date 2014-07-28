from django.conf.urls import patterns, include, url
from tatuazhkiev.views import hello, my_homepage_view, current_datetime, hours_ahead
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'tatuazhkiev.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
	('^hello/$', hello),
	('^$', my_homepage_view),
	('^date/$', current_datetime),
	(r'^time/plus/(\d{1,2})/$', hours_ahead),
	
)