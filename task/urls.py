
from django.conf.urls import url, include
from django.contrib import admin
#from django.contrib.auth.views import views as auth_views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^myapp/',include('myapp.urls')),


]
