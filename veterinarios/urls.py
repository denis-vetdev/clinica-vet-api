from rest_framework.routers import DefaultRouter
from .views import VeterinarioViewSet

router = DefaultRouter()
router.register(r'veterinarios', VeterinarioViewSet)

urlpatterns = router.urls