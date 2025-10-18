from rest_framework import serializers
from galeria.models import Galeria

class GaleriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Galeria
        fields = '__all__'
        read_only_fields = ['id', 'fecha']  
    
    