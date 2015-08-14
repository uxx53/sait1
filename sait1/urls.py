from django.conf.urls import patterns, include, url
from django.contrib import admin


urlpatterns = [
  #  url(r'^app_main/', include('app_main.urls', namespace='main1')),
    url(r'^', include('app_main.urls', namespace='main1')),
    url(r'^admin/', include(admin.site.urls)),
]
