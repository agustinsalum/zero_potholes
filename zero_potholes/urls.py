
"""
Configuración de URLs para el proyecto zero_potholes
"""

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('zero_potholes_app.api.urls')),  # API endpoints
]
