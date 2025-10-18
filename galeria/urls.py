from rest_framework import routers
from .api import GaleriaViewSet 

router = routers.DefaultRouter()

router.register(r'galeria', GaleriaViewSet)

urlpatterns = router.urls
