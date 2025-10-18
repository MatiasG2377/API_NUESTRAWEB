from rest_framework import routers
from .api import FechasViewSet

router = routers.DefaultRouter()

router.register(r'fechas', FechasViewSet)

urlpatterns = router.urls