
"""
Garantiza que las rutas definidas en router.py estén disponibles públicamente en la aplicación.
"""


from django.urls import path, include
from .router import router

urlpatterns = [
    # Usamos "include" para que Django reconozca las rutas y puedan usarse.
    path('', include(router.urls)),
]
