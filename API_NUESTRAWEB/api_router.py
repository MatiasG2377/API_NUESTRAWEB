from rest_framework import routers
from fechas.api import FechasViewSet
from galeria.api import GaleriaViewSet

router = routers.DefaultRouter()

# Registra todos los endpoints aquí
router.register(r'galeria', GaleriaViewSet)
router.register(r'fehchas', FechasViewSet)

urlpatterns = router.urls
