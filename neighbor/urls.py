from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^login/', views.user_login, name='login'),
    url(r'^logout/$', views.user_logout, name='logout'),
    url(r'^search/', views.search, name="search"),
    url(r'^view/$', views.neighborhoods, name='neighborhoods'),
    url(r'^view/user/(?P<id>\d+)/$', views.view_user, name='view_user'),
    url(r'^view/business/(?P<id>\d+)/$', views.view_business, name='view_business'),
    url(r'^view/(?P<id>\d+)/$', views.show_neighborhood, name='show_neighborhood'),
    url(r'^view/(?P<id>\d+)/edit/', views.edit_neighborhood, name='edit_neighborhood'),
    url(r'^view/(?P<id>\d+)/delete/', views.delete_neighborhood, name='delete_neighborhood'),
    url(r'^view/(?P<id>\d+)/posts/', views.posts, name='posts'),
    url(r'^create_neighborhood/', views.create_neighborhood, name='create_neighborhood'),
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',views.activate, name='activate'),
    url(r'^confirm/$', views.confirm, name='confirm')
]
