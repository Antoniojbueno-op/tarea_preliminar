from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView ,ListView,CreateView,DeleteView,UpdateView
from rest_framework import generics
from apps.modelo_coche.serializers import ModeloSerializer
from apps.modelo_coche.models import modelo_de_coche

# Create your views here.
class crear_views(CreateView):
    template_name = 'crear/crear_modelo.html'
    fields=('__all__')
    model=modelo_de_coche
    success_url=reverse_lazy('url:crear')
class eliminar_view(DeleteView):
    template_name="eliminar/eliminar.html"
    model=modelo_de_coche

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        success_url = reverse_lazy('url:lista')
        self.object.delete()
        return HttpResponseRedirect(success_url)

#API_Crear
class modeloCreateApiView(generics.CreateAPIView):
    serializer_class = ModeloSerializer

#API_Eliminar
class modeloDestroyApiView(generics.DestroyAPIView):
    serializer_class = ModeloSerializer
    queryset = modelo_de_coche.objects.all()

#API_Editar
class modeloUpdateApiView(generics.UpdateAPIView):
    serializer_class = ModeloSerializer
    queryset = modelo_de_coche.objects.all()
#API_Listar
class modeloListApiView(generics.ListAPIView):   
                
    serializer_class = ModeloSerializer
    def get_queryset(self):
        return modelo_de_coche.objects.all()