from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^$', 'master.views.index', name='index'),
    )

