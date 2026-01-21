"""
Define las rutas de la API y las vincula con los ViewSets.
Genera automáticamente endpoints CRUD RESTful.
"""

from rest_framework import routers
from .viewsets import (
    ReportViewSet,
    ReportStatusViewSet,
    ReportSeverityViewSet,
    CityViewSet,
    ProvinceViewSet,
)

router = routers.SimpleRouter()

router.register("reports", ReportViewSet, basename="report")
router.register("report-status", ReportStatusViewSet, basename="report-status")
router.register("report-severity", ReportSeverityViewSet, basename="report-severity")
router.register("cities", CityViewSet, basename="city")
router.register("provinces", ProvinceViewSet, basename="province")

