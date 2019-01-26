from django.conf.urls import url,include
from .views import *
app_name='utils'
urlpatterns = [
    url(r'^$',home,name='home'),
    url(r'^merge/$',merge,name='merge'),
    url(r'^split/$',split,name='split'),
    url(r'^rotate/$',rotate,name='rotate'),
    url(r'^split/do/$',split_do,name='split_do'),
    url(r'^merge/do/$',merge_do,name='merge_do'),
    url(r'^download/$',download,name='download'),
    url(r'^merge/final',merge_final,name='merge_final'),
]