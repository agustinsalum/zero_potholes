"""
Configuración de la aplicación zero_potholes_app.
"""

from django.apps import AppConfig


class ZeroPotholesAppConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "zero_potholes_app"
    verbose_name = "Zero Potholes"
