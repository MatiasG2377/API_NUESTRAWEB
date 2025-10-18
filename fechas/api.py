from rest_framework import viewsets, permissions
from .models import Fechas
from .serializers import FechasSerializer
from rest_framework.pagination import PageNumberPagination
from drf_spectacular.utils import extend_schema

class FechaPaginator(PageNumberPagination):
    page_size = 10  
    page_size_query_param = 'page_size'
    max_page_size = 50

@extend_schema(
    tags=["Fechas"],
    operation_id="Fechas.Endpoints que permiten listar, ver, crear, actualizar y eliminar fechas especiales de nuestra vida juntos. "
)
class FechasViewSet(viewsets.ModelViewSet):
    queryset = Fechas.objects.all().order_by('-fecha')
    serializer_class = FechasSerializer
    permission_classes = [permissions.AllowAny]

    










