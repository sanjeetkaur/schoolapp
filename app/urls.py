from django.conf.urls import patterns, url

from app import views

urlpatterns = patterns('',
    url(r'^index/', views.index, name='first'),
    url(r'^display/', views.display, name='final'),
)
