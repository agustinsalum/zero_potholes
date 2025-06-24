
"""

Defines the API routes and links them to the viewsets.

"""

from rest_framework import routers
from .viewsets import ReportViewSet, ReportStatusViewSet, ReportSeverityViewSet, CityViewSet, ProvinceViewSet

router = routers.SimpleRouter()

# In this case it is appended to the route of the app's urls
# router.register(prefix, viewset, basename=None)
router.register('reports', ReportViewSet, basename='report')
router.register('report-status', ReportStatusViewSet, basename='report-status')
router.register('report-severity', ReportSeverityViewSet, basename='report-severity')
router.register('cities', CityViewSet, basename='city')
router.register('provinces', ProvinceViewSet, basename='province')
