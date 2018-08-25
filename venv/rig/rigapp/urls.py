from django.conf.urls import url
from . import views
import os

urlpatterns =[
    url(r'^$',views.index,name='index'),
    url(r'^submit$',views.submit,name='submit'),
    url(r'^download$',views.down,name='download'),
    ]
#r means regex start and ^ means start of line and $ is end of line
from django.conf.urls import url
from . import views
import os

urlpatterns =[
    url(r'^$',views.index,name='index'),
    url(r'^submit$',views.submit,name='submit'),
    url(r'^download$',views.down,name='download'),
    ]
#r means regex start and ^ means start of line and $ is end of line
