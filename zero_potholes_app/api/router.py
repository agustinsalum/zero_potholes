
"""

Defines the API routes and links them to the viewsets.

"""

from rest_framework import routers
from .viewsets import ReportViewSet

router = routers.SimpleRouter()

# In this case it is appended to the route of the app's urls
# router.register(prefix, viewset, basename=None)
router.register('reports', ReportViewSet, basename='report')