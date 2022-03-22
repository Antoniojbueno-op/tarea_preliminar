from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView ,ListView,CreateView,DeleteView,UpdateView
from .serializers import *
from rest_framework import generics

from apps.marca_coche.models import Marca_coche
# Create your views here.
class crear_views(CreateView):
    template_name = 'crear/crear_marca.html'
    fields=('__all__')
    model=Marca_coche
    success_url=reverse_lazy('url:crear')
class eliminar_view(DeleteView):
    template_name="eliminar/eliminar.html"
    model=Marca_coche

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        success_url = reverse_lazy('url:lista')
        self.object.delete()
        return HttpResponseRedirect(success_url)
class MarcaListApiView(generics.ListAPIView):
    serializer_class = MarcaSerializer

    def get_queryset(self):
        return Marca_coche.objects.all()

#API_Crear
class MarcaCreateApiView(generics.CreateAPIView):
    serializer_class = MarcaSerializer

#API_Eliminar
class MarcaDestroyApiView(generics.DestroyAPIView):
    serializer_class = MarcaSerializer
    queryset = Marca_coche.objects.all()

#API_Modificar
class MarcaUpdateApiView(generics.RetrieveUpdateAPIView):
    serializer_class = MarcaSerializer
    queryset = Marca_coche.objects.all()
#API_Listar
class MarcaListApiView(generics.ListAPIView):   
                
    serializer_class = MarcaSerializer
    def get_queryset(self):
        return Marca_coche.objects.all()