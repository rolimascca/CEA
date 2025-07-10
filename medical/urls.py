from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import AlergiaViewSet, EnfermedadViewSet, estudiantes_por_alergia

# Configuración del router
router = DefaultRouter()
router.register(r'alergias', AlergiaViewSet, basename='alergias')
router.register(r'enfermedades', EnfermedadViewSet, basename='enfermedades')

# Configuración de urlpatterns adicionales
urlpatterns = [
    # Ruta personalizada para filtrar estudiantes por tipo de alergia
    path('reportes/alergias/<str:tipo_alergia>/', estudiantes_por_alergia, name='estudiantes_por_alergia'),
]

# Combinar las rutas del router con las rutas adicionales
urlpatterns += router.urls