
from django.conf.urls import url,include
from django.contrib import admin
#from django.contrib.auth.views import views as auth_views
from django.contrib import admin
from django.views.generic import TemplateView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^myapp/', include('myapp.urls')),
    #url('^social-auth/', include('social.apps.django_app.urls', namespace='social')),

]
