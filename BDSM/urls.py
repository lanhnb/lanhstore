from django.contrib import admin
from django.urls import path, include
from home.views import handler404, handler500
from django.conf.urls import handler404, handler500
from django.conf.urls.static import static
from django.conf.urls import url
from django.conf import settings
from django.urls import re_path
from django.views.static import serve
import search

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('home.urls')),
    path('search/', include('search.urls')),
    path('shop/', include('shop.urls')),
    url(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
    url(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT}),

]

handler404 = 'home.views.handler404'
handler500 = 'home.views.handler500'


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns = urlpatterns + static( settings.STATIC_URL, document_root=settings.STATIC_ROOT )
