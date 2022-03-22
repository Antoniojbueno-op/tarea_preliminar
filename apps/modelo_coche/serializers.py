from rest_framework import serializers

from apps.modelo_coche.models import modelo_de_coche


class ModeloSerializer(serializers.ModelSerializer):
    class Meta:
        model=modelo_de_coche
        fields=("__all__")