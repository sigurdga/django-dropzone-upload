from django.conf.urls import patterns, include, url
from fileupload.views import PictureCreateView

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', PictureCreateView.as_view(), name='home'),
    url(r'^admin/', include(admin.site.urls)),
)
