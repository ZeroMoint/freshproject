from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^register/$', views.register, name='register'),
    url(r'^register_handle/$', views.register_handle, name='register_handle'),
    url(r'^login/$', views.login, name='login'),
    url(r'^login_handle/$', views.login_handle, name='login_handle'),
    url(r'^info/$', views.info, name='info'),
    url(r'^site/$', views.site, name='site'),
    url(r'^order/$', views.order, name='order'),

]