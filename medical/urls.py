from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'alergias', views.AlergiaViewSet)
router.register(r'enfermedades', views.EnfermedadViewSet)

urlpatterns = router.urls
