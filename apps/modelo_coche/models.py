from django.db import models


# Create your models here.
class modelo_de_coche(models.Model):
    
   
    modelo=models.CharField(("Modelo de coche"), max_length=100)
    

    class Meta:
        verbose_name = ("modelo")
        verbose_name_plural = ("modelos")

    def __str__(self):
        return self.modelo+" "+str(self.id)