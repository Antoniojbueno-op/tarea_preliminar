from csv import field_size_limit
from dataclasses import fields
from .forms import cocheform
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView ,ListView,CreateView,DeleteView,UpdateView,DetailView
# Create your views here.
from .models import *
from rest_framework import generics
class Menu(TemplateView):
    template_name='coche/menu.html'
    
class Listacar(ListView):
    """Lista cohes"""
    template_name='Lista/lista.html'
    model=Coche
    context_object_name='lenlista'
    
    
#    def get_queryset(self):
#        model=Coche
#        busqueda_sql=self.kwargs['tipo_de_lista']
#        
#        lista=Coche.objects.filter(
#            marca__marca=busqueda_sql
#        )
#        return model
#class eliminar(DeleteView):

class update_view(UpdateView):
    template_name="actualizar/actualizar.html"
    
    model=Coche
    fields=[
        "marca",
        "modelo",
        "fecha",
        "Telefono",
        "matricula",
        ]
    success_url=reverse_lazy('url:lista')
    def post(self, request, *args, **kwargs):
        self.objects=self.get_object()
        return super().post(request, *args, **kwargs)
class eliminar_view(DeleteView):
    template_name="eliminar/eliminar.html"
    model=Coche

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        success_url = reverse_lazy('url:lista')
        self.object.delete()
        return HttpResponseRedirect(success_url)
class crear_views(CreateView):
    template_name = 'crear/create.html'
    fields=('__all__')
    model=Coche
    success_url=reverse_lazy('url:lista')
class filter_marca(ListView):
    template_name='filtro/filtro_marca.html'
    ordering="id"
    def get_queryset(self):
        palabra_clave = self.request.GET.get("kword",'')
        
        lista=Coche.objects.filter(
            marca__marca__icontains=palabra_clave
            )
        if  str(lista)=="<QuerySet []>":
                
            self.template_name='error/404_modelo.html'
            
        return lista

            
        
class filter_telefono(ListView):
    template_name='filtro/filtro_telefono.html'
    ordering="id"
    def get_queryset(self):
        palabra_clave = self.request.GET.get("kword",'')
        lista=Coche.objects.filter(
            Telefono__icontains=palabra_clave
        )
        if  str(lista)=="<QuerySet []>":
                
                self.template_name='error/404_modelo.html'
            
        return lista
        
            
            
class filter_modelo(ListView):
    template_name='filtro/filtro_modelo.html'
    ordering="id"
    def get_queryset(self):
        palabra_clave = self.request.GET.get("kword",'')
        lista=Coche.objects.filter(
            modelo__modelo__icontains=palabra_clave
        )
        if  str(lista)=="<QuerySet []>":
                
                self.template_name='error/404_modelo.html'
            
        return lista

            
class filter_id(ListView):
    template_name='filtro/filtro_id.html'
    ordering="id"
    def get_queryset(self):
        palabra_clave = self.request.GET.get("kword",'')
        
        
        try:
            
            lista=Coche.objects.filter(
                id=palabra_clave
            )
        except:
            
            lista=Coche.objects.filter(
            id__icontains=palabra_clave
        )
            
        finally:
            
            if  str(lista)=="<QuerySet []>":
                
                self.template_name='error/404_id.html'
            
            return lista
class filter_fecha(ListView):
    template_name='filtro/filtro_fecha.html'
    ordering="id"
    def get_queryset(self):
        palabra_clave = self.request.GET.get("kword",'')
        
        
        try:
            
            lista=Coche.objects.filter(
                fecha__range=["2000-01-01",palabra_clave]
            )
        except:
            
            lista=Coche.objects.filter(
            fecha__icontains=palabra_clave
        )
            
        finally:
            
            if  str(lista)=="<QuerySet []>":
                
                self.template_name='error/404_fecha.html'
            
            return lista
class filter_matricula(ListView):
    template_name='filtro/filtro_matricula.html'
    ordering="id"
    def get_queryset(self):
        palabra_clave = self.request.GET.get("kword",'')
        lista=Coche.objects.filter(
            matricula__icontains=palabra_clave
            )
        if  str(lista)=="<QuerySet []>":
                
            self.template_name='error/404_matricula.html'
            
        return lista
class filter_matricula(ListView):
    template_name='filtro/filtro_matricula.html'
    ordering="id"
    def get_queryset(self):
        palabra_clave = self.request.GET.get("kword",'')
        
        
        try:
            
            lista=Coche.objects.filter(
                matricula=palabra_clave
            )
        except:
            
            lista=Coche.objects.filter(
            matricula__icontains=palabra_clave
        )
            
        finally:
            
            if  str(lista)=="<QuerySet []>":
                
                self.template_name='error/404_matricula.html'
            
            return lista

class filter_key(ListView):
    template_name='filtro/filtro_keys.html'
    
    diccionario={}
    for key,vaules in Coche.objects.values_list("marca__marca","modelo__modelo"):
        
        diccionario.setdefault(key, []).append(vaules)
    """
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        #No se me a ocurrido otra manera
        
        
        
        palabra_clave = self.request.GET.get("kword",'')
        if  palabra_clave  in self.diccionario.keys():
            print("entro")
            return self.diccionario[palabra_clave]
        else:
            print("entro2")
            
            self.template_name='error/404_key.html'
            return self.diccionario
    """
    def get_queryset(self):
        print("queryset")
        return Coche.objects.all()
def filtro_key(request):
    diccionario={}
    palabra_clave = request.GET.get("kword",'')
    
    for key,vaules in Coche.objects.values_list("marca__marca","modelo__modelo"):
        
        diccionario.setdefault(key, []).append(vaules)
    print(diccionario)
    if palabra_clave in diccionario.keys():
        
        
        """
        Nota para yo del futuro
        Lo siguiente que tiens que hacer es crear el html correcto del las keys y la api
        Suerte
        """
        
        return render(request, 'filtro/filtro_keys.html' ,{"dic":{palabra_clave:diccionario[palabra_clave]}})
    else:
        
        return render(request, 'filtro/filtro_keys.html' ,{"dic":diccionario})
"""
def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context['applications'] = Application.objects.all()
    context['devices'] = Device.objects.all()
    return context


"""     
from .serializers import *
class Cocheapilist(generics.ListAPIView):   
                
    serializer_class = Coche_serializer
    def get_queryset(self):
        return Coche.objects.all()
class crear_views_api(generics.CreateAPIView):
    form_class=cocheform
    serializer_class = Coche_add_serializer
    
class delete_view_api(generics.DestroyAPIView):
    serializer_class = Coche_serializer
    queryset =Coche.objects.all()
class update_view_api(generics.UpdateAPIView):
    form_class=cocheform
    serializer_class = Coche_serializer_update
    queryset =Coche.objects.all()