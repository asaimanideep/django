from django.conf.urls import url,include
from . import views
from django.contrib.auth.views import login ,logout
app_name='myapp'
urlpatterns=[
    url(r'^$',views.home),
    url(r'^index/',views.index),
    url(r'^profiles/',views.profiles),
    #url(r'^profiles/(?P<pk>\d+)$',views.getdetails),
    url(r'^getdetails/',views.getdetails),
    url(r'^login/$', login, {'template_name': 'myapp/login.html'}),
    url(r'^logout/$', logout ,{'template_name': 'myapp/logout.html'}),
    url(r'^register/$', views.register, name='register'),


]