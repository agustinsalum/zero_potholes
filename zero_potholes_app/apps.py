
"""
Define la configuración de la aplicación Django llamada zero_potholes_app
"""

from django.apps import AppConfig

class ZeroPotholesAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    # Define el nombre de la aplicación
    name = 'zero_potholes_app'
