from django.conf.urls import patterns, include, url
from django.contrib import admin


urlpatterns = patterns('',
    url(r'^app/', include('app.urls')),
    # Examples:
    #url(r'^$', 'school.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),


  #  url(r'^$', 'app.views.index'),
    url(r'^admin/', include(admin.site.urls)),
)
