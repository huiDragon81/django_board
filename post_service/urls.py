from django.conf.urls import patterns, url

from post_service.views import post_list

urlpatterns = patterns('',
                       url(r'^$', post_list),
                       )