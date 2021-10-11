from django.contrib import admin
from django.urls import path, include
from django.conf.urls import handler404, handler500
from django.conf.urls.static import static
from django.conf import settings

import search

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('home.urls')),
    path('search/', include('search.urls')),
    path('shop/', include('shop.urls')),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns = urlpatterns + static( settings.STATIC_URL, document_root=settings.STATIC_ROOT )
    # handler404 = 'home.views.error'
    # handler500 = 'home.views.error'
