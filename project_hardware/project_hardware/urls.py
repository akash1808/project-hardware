from django.conf.urls import patterns, include, url

from django.contrib import admin
from componentAPI import views
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'project_hardware.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
#    url(r'^$', 'componentAPI.views.index'),
#    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
    url(r'^api/v1/components/$', views.post_collection),
    url(r'^api/v1/components/(?P<pk>[0-9]+)/$', views.post_element),
)
