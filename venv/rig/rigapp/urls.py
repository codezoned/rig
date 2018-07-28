from django.conf.urls import url
from . import views

urlpatterns =[
    url(r'^$',views.hellopage,name='hellopage')]
#r means regex start and ^ means start of line and $ is end of line
