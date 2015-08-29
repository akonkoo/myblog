from django.conf.urls import include, url

from . import views, feed


urlpatterns = [
    url('^$', views.BlogIndex.as_view(template_name = 'blog/index.html'), 
    	name = 'index'),
    url(r'^archives', views.BlogIndex.as_view(template_name = 'blog/archives.html'),
    	name = 'archives'),
    url(r'^entry/(?P<pk>\d+)$', views.BlogDetail.as_view(), name = 'detail'),
    url(r'^tag/(?P<pk>\d+)$', 'blog.views.tagdetail', name='tagdetail'),
    url(r'^about/$', 'blog.views.about', name='about'),
    url(r'^feed/$', feed.RssFeed(), name = 'feed'),
]
