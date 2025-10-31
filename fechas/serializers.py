from rest_framework import serializers
from fechas.models import Fechas

class FechasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fechas
        fields = '__all__'
        read_only_fields = ['id']  
        