
from unicodedata import name
from xml.etree.ElementInclude import include
from django.contrib import admin
from django.urls import path
from requests import delete
from .views import *


urlpatterns = [
    # path('admin/', admin.site.urls),
    path('',index.as_view(),name='index'),
    path('login',loginA.as_view(),name='login'),
    path('reg',loginR.as_view(),name='reg'),
    path('logout',logout.as_view(),name='out'),
    path('savep',saveplace.as_view(),name='savep'),
    # path('deleteplace',deleteplace.as_view(),name='deleteplace'),
    path('deleteplace', delete,name='deleteplace'),
    path('editplace', getInfo, name='editplace'),
    # path('ajax/', include('ajax.urls')),  


]
