from django.conf.urls import url, include
from . import views
# from django.contrib.auth import views as auth_views
import views as core_views


urlpatterns = [
    url(r'^signup/$', views.signup, name='signup'),
    url(r'profile/', views.profile_view, name='view_profile'),
    url(r'', views.home, name='home'),
]







# url(r'^accounts/', include('registration.backends.simple.urls')),
# url(r'^login/$', auth_views.login),
# url(r'^logout/$', auth_views.logout),
