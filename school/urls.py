from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'school.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),


    url(r'^app/$', 'app.views.first'),
    url(r'^admin/', include(admin.site.urls)),
)
