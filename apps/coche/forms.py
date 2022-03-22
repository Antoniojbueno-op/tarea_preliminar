from cProfile import label
from django import forms
from .models import *
class marcacoche(forms.ModelForm):
    class Meta:
        models=Marca_coche
        fields=[
            "marca"
        ]
        labels={"marca":"marca"}
class modeloCoche(forms.ModelForm):
    class Meta:
        modelo=modelo_de_coche
        fields=["modelo"]
        labels={"modelo":"modelo"}
class cocheform(forms.ModelForm):
    class Meta:
        model=Coche
        fields=("__all__")
        widgets  = { 
            'modelos' :  forms . Select (), 
            'marca' :  forms . Select (), 
        }