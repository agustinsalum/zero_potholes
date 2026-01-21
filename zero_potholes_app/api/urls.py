
"""
Expone las rutas definidas en router.py a nivel de aplicación.
"""

from django.urls import path, include
from .router import router

urlpatterns = [
    path("", include(router.urls)),
]
