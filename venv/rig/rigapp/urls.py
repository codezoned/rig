from django.conf.urls import url
from . import views
import os
path=os.path.abspath(r"F:\New folder\rig3\venv\rig\rigapp\Badge.pdf")
urlpatterns =[
    url(r'^$',views.index,name='index'),
    url(r'^submit',views.submit,name='submit'),
    ]
#r means regex start and ^ means start of line and $ is end of line
