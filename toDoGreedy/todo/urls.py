from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<bookmark_id>[0-9]+)/$', views.search, name='search'),
    url(r'^(?P<bookmark_id>[0-9]+)/results/$', views.results, name='results'),
    url(r'^(?P<bookmark_id>[0-9]+)/add/$', views.add, name='add'),
]
