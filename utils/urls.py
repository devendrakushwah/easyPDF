from django.conf.urls import url,include
from .views import *
app_name='utils'
urlpatterns = [
    url(r'^$',home,name='home'),
    url(r'^merge/$',merge,name='merge'),
    url(r'^split/$',split,name='split'),
    url(r'^rotate/$',rotate,name='rotate'),
]