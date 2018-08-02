from django.conf.urls import url
from . import views

urlpatterns =[
    url(r'^$',views.index,name='index'),
    url(r'^submit',views.submit,name='submit'),]
#r means regex start and ^ means start of line and $ is end of line
