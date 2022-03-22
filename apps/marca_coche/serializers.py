from rest_framework import serializers

from apps.coche.models import Marca_coche
class MarcaSerializer(serializers.ModelSerializer):
    class Meta:
        model=Marca_coche
        fields=("__all__")