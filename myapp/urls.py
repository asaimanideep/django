from django.conf.urls import url,include
from . import views

urlpatterns=[
    url(r'^$',views.home),
    url(r'^index/',views.index),
    url(r'^profiles/',views.profiles),
    url(r'^getdetails/',views.getdetails),
]