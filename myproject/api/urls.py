from rest_framework.routers import DefaultRouter
from .views import GaleriaViewSet, FechaViewSet

router = DefaultRouter()
router.register(r'galeria', GaleriaViewSet)
router.register(r'fecha', FechaViewSet)

urlpatterns = router.urls
