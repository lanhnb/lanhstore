from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LoginView, LogoutView
from .models import Post
from django.views.generic import ListView, DetailView


urlpatterns = [
    path('', ListView.as_view(
        queryset=Post.objects.all().order_by('-date'),
        template_name='pages/home.html',
        context_object_name='Posts',
        paginate_by=8), name='home'),
    path('<int:pk>/', views.post, name='post'),
    path('contact/', views.contact, name ='contact'),
    path('register/', views.register, name = 'register'),
    path('login/', auth_views.LoginView.as_view(template_name = 'pages/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='/'), name='logout'),

]