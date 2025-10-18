# galeria/views.py

from rest_framework import viewsets, permissions
from rest_framework.parsers import MultiPartParser, FormParser
from drf_spectacular.utils import extend_schema, OpenApiTypes, OpenApiParameter 
from .models import Galeria
from .serializers import GaleriaSerializer

from rest_framework.pagination import PageNumberPagination

class GaleriaPaginator(PageNumberPagination):
    page_size = 10  
    page_size_query_param = 'page_size'
    max_page_size = 50


@extend_schema(
    tags=["Galeria"],
    request={
        "multipart/form-data": { 
            "type": "object",
            "properties": {
                "image": {"type": "string", "format": "binary", "description": "Archivo de imagen a subir"}, 
                "titulo": {"type": "string", "description": "Título de la imagen"},
            },
            "required": ["image", "titulo"] 
        }
    },
    description="Subir una imagen con título"
)
class GaleriaViewSet(viewsets.ModelViewSet):
    queryset = Galeria.objects.all().order_by('-fecha')
    serializer_class = GaleriaSerializer
    permission_classes = [permissions.AllowAny]
    parser_classes = [MultiPartParser, FormParser]
    pagination_class = GaleriaPaginator