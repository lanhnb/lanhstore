from sys import path
from django.conf.urls import url



from .views import searchposts

app_name ='search'
urlpatterns = [
     url(r'^$', searchposts, name='searchposts'),

]
