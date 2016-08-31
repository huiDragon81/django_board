from django.conf.urls import include, url
from django.contrib import admin

import post_service

urlpatterns = [
    # Examples:
    # url(r'^$', 'django_board.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^board/', include('post_service.urls')),
    url(r'^user/', include('user_manager.urls')),
]
