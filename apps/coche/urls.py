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
app_name="url"
urlpatterns = [
    path('menu/', views.Menu.as_view(),name='home'),
    path('listado/',views.Listacar.as_view(),name='lista'),
    path('update/<pk>',views.update_view.as_view(),name='update'),
    path('eliminar/<pk>',views.eliminar_view.as_view(),name='delete'),
    path('crear/', views.crear_views.as_view(),name='crear'),
    path('filtro_marca/',views.filter_marca.as_view(),name='filtro_marca'),
    path('filtro_id/',views.filter_id.as_view(),name='filtro_id'),
    path('filtro_fecha/',views.filter_fecha.as_view(),name='filtro_fecha'),
    path('filtro_telefono',views.filter_telefono.as_view(),name='filtro_telefono'),
    path('filtro_modelo/',views.filter_modelo.as_view(),name='filtro_modelo'),
    path('filtro_matricula/',views.filter_matricula.as_view(),name='filtro_matricula'),
    path("key_filtro/",views.filtro_key,name='key'),
    path('apilist/',views.Cocheapilist.as_view(),name='api_list'),
    path('apiadd/',views.crear_views_api.as_view(),name='api_add'),
    path('apidelete/<pk>/',views.delete_view_api.as_view(),name='api_delete'),
    path('apiupdate/<pk>/',views.update_view_api.as_view(),name='api_update'),
    
    
]
#path('eliminar/<pk>',views.eliminar.as_view(),name='eliminar')