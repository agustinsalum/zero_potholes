
"""

Ensures that the routes defined in router.py are publicly available in the application.

"""

from django.urls import path, include
from .router import router

urlpatterns = [
    path('', include(router.urls)),
]
