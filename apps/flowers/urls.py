from django.conf.urls import url

from django.conf import settings
from . import views

urlpatterns = [
    url(r'^$', views.index, name="home"),        
    url(r'^help$', views.help, name="help"),        
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root':
        settings.MEDIA_ROOT}),
]

