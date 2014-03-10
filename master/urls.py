from django.conf.urls import patterns, include, url
from django.conf import settings

from master import views

urlpatterns = patterns('master.views',
    url(r'^$', 'index', name='index'),
)
