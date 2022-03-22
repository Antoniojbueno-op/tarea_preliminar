from pyexpat import model
from django.db import models
from apps.marca_coche.models import Marca_coche
from apps.modelo_coche.models import modelo_de_coche
from phone_field import PhoneField
# Create your models here.

class Coche(models.Model):
    
    marca=models.ForeignKey(Marca_coche,on_delete=models.CASCADE)
    modelo=models.ForeignKey(modelo_de_coche,on_delete=models.CASCADE,blank=True)
    fecha=models.DateField(null=True, blank=True)
    Telefono=PhoneField(null=True, blank=True)
    matricula=models.CharField("Matricula",max_length=7,unique=True)
    def __str__(self):
        return str(self.marca)+" "+str(self.fecha)+" "+str(self.Telefono)+" "+self.matricula