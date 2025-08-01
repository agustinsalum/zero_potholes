
"""

Define las rutas de la API y las vincula con los viewsets

"""

from rest_framework import routers
from .viewsets import ReportViewSet, ReportStatusViewSet, ReportSeverityViewSet, CityViewSet, ProvinceViewSet

router = routers.SimpleRouter()

# Usamos register() para vincular una ruta de URL con un ViewSet (crear, leer, actualizar, eliminar)
# Genera automáticamente todas las rutas CRUD
# En este caso, se agrega a la ruta del archivo urls de la app
# router.register(prefijo, viewset, basename=None)
router.register('reports', ReportViewSet, basename='report')
router.register('report-status', ReportStatusViewSet, basename='report-status')
router.register('report-severity', ReportSeverityViewSet, basename='report-severity')
router.register('cities', CityViewSet, basename='city')
router.register('provinces', ProvinceViewSet, basename='province')
