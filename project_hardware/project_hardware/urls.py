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
    url(r'^users/', views.UserList.as_view()),
    url(r'^users/(?P<pk>[0-9]+)/$', views.UserDetail.as_view()),
)
