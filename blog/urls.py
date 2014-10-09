from django.conf.urls import patterns, url

from blog import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^(?P<article_id>\d+)/$', views.detail, name='detail'),
    url(r'^author/(?P<author_id>\d+)/$', views.author, name='author'),
    url(r'^tag/(?P<tag_id>\d+)/$', views.tag, name='tag'),
    url(r'^comment/(?P<article_id>\d+)/$', views.comment, name='comment'),
)