from django.urls import path,include
from django.contrib import admin
from . import views


urlpatterns=[
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/', include('accounts.urls')),
    path("display",views.result,name="result"),
    path('',views.home,name="home"),
    
]