from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LoginView, LogoutView
from .models import Product
from django.views.generic import ListView, DetailView
from django.conf.urls import url
from django.conf.urls.static import static
from .views import search, index, productView, checkout



urlpatterns = [
    path('',views.index, name ='ShopHome' ),
    path('search/', views.search, name='search'),
    path("products/<int:myid>", views.productView, name='ProductView'),
    path('categogy/<int:myid>', views.productView, name='Categogy'),
    path('checkout/', views.checkout, name = 'checkout'),
    path('tracker/', views.tracker, name = 'tracker'),


]


