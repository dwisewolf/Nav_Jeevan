from django.urls import path
from django.conf.urls import url
from django.views.decorators.csrf import csrf_exempt
from . import views
from django.contrib.auth import views as auth_views
from django.views.generic.base import TemplateView

urlpatterns = [
    #Admin Panel
    path('home/create/', views.create,name='create'),
    url(r'^adminhome/$', views.home, name='home'),
    url(r'^stulist(?P<id>\d+)/$', views.detail_view,name='stulist'),
    url(r'^adminlogin/$', auth_views.login, {'template_name': 'login.html'}, name='adminlogin'),
    url(r'^adminlogout/$', auth_views.logout, {'template_name': 'logged_out.html'}, name='adminlogout'),
    #Student Panel
    url(r'^$', TemplateView.as_view(template_name='index.html'), name='index'),
    path('studentlogin/', views.studata,name='studentlogin'),
    path('stulogout/', views.stulogout,name='stulogout'),
]
