from django.urls import path
from . import views

urlpatterns = [
    path('reporte-medico/', views.reporte_medico, name='reporte-medico'),
    path('reportes-html/', views.reportes_html, name='reportes-html'),
]
