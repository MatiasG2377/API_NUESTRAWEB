from rest_framework import serializers
from .models import Galeria, Fecha

class GaleriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Galeria
        fields = '__all__'


class FechaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fecha
        fields = '__all__'
