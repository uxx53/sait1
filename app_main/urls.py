__author__ = 'BUR'
from django.conf.urls import url
from . import views

urlpatterns = [
 #   url(r'^$', views.ret1),
    url(r'^$', views.index, name='index'),
  #  url(r'^(?P<fio_id>[0-9]+)/$', views.detail, name='detail'),
    url(r'^(?P<fio_id>[0-9]+)/$', views.get_name, name='name1'),
    url(r'^(?P<fio_id>[0-9]+)/vote/$', views.vote, name='vote'),
    url(r'^(?P<fio_id>[0-9]+)/results/$', views.results, name='results'),
    url(r'^images/$', views.sea1),
    url(r'^thanks/$', views.contact),

]
