from email.policy import default
from django.db import models

# Create your models here.
class Marca_coche(models.Model):
    marca=models.CharField("Marca de coche",max_length=100)
    
    
    class Meta:
        verbose_name = ("Marca de coche")
        verbose_name_plural = ("Marcas de coches")
        
    
    def __str__(self):
        return str(self.id)+"-"+self.marca +" "+"\n"