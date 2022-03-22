"""actividad_automoviles URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from . import views
app_name="marca"
urlpatterns=[
    path("crear_marca/",views.crear_views.as_view()),
    path("eliminar_marca/<pk>",views.eliminar_view.as_view(),name="eliminar"),
    path('apilist_marca/',views.MarcaListApiView.as_view(),name='api_list'),
    path('apiadd_marca/',views.MarcaCreateApiView.as_view(),name='api_add'),
    path('apidelete_marca/<pk>/',views.MarcaDestroyApiView.as_view(),name='api_delete'),
    path('apiupdate_marca/<pk>/',views.MarcaUpdateApiView.as_view(),name='api_update'),
    
    
]