from django.shortcuts import render
from rest_framework import viewsets
from .models import Galeria, Fecha
from .serializers import GaleriaSerializer, FechaSerializer

class GaleriaViewSet(viewsets.ModelViewSet):
    queryset = Galeria.objects.all()
    serializer_class = GaleriaSerializer


class FechaViewSet(viewsets.ModelViewSet):
    queryset = Fecha.objects.all()
    serializer_class = FechaSerializer
