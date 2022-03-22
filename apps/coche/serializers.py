from rest_framework import serializers

from apps.modelo_coche.models import modelo_de_coche
from apps.marca_coche.models import Marca_coche

from apps.coche.models import Coche


class modelo_Coche(serializers.ModelSerializer):
    def create(self, validated_data):
        return modelo_de_coche.objects.create(**validated_data)
    class Meta:
        model=modelo_de_coche
        fields=["modelo"]
        
        
        
class marca_coche(serializers.ModelSerializer):
    def create(self, validated_data):
        return Marca_coche.objects.create(**validated_data)
    class Meta:
        model=Marca_coche
        fields=["marca"]
        
        
        
class Coche_serializer(serializers.ModelSerializer):
    marca=marca_coche()
    modelo=modelo_Coche()
    read_only=True
    

    class Meta:
        model = Coche
        fields=(
            "marca",
            "modelo",
            "fecha",
            "Telefono",
            "matricula",
            
        )
        
        
        
        
class Coche_add_serializer(serializers.ModelSerializer):
    marca=marca_coche().create
    modelo=modelo_Coche().create 

    class Meta:
        model = Coche
        fields=(
            "marca",
            "modelo",
            "fecha",
            "Telefono",
            "matricula",
            
        )
class Coche_serializer_update(serializers.ModelSerializer):
    marca=marca_coche().update
    modelo=modelo_Coche().update 

    class Meta:
        model = Coche
        fields=(
            "marca",
            "modelo",
            "fecha",
            "Telefono",
            "matricula",
            
        )
    

    