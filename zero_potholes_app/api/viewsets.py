
"""

Define las vistas que gestionan la lógica para operaciones CRUD sobre los modelos

"""

from rest_framework import viewsets, status

from rest_framework.decorators import action
from rest_framework.response import Response

from rest_framework.permissions import AllowAny


from zero_potholes_app.models import Report, ReportStatus, ReportSeverity, City, Province
from zero_potholes_app.api.serializers import (
    PublicReportSerializer,
    ReportSerializer,
    ReportStatusSerializer,
    ReportSeveritySerializer,
    CitySerializer,
    ProvinceSerializer
)

class ReportViewSet(viewsets.ModelViewSet):
    queryset = Report.objects.all()
    serializer_class = ReportSerializer

    """ Permite al usuario autenticado listar los reportes asignados a él """

    @action(detail=False, methods=['get'], url_path='assigned')
    def assigned_to_me(self, request):
        reports = Report.objects.filter(assigned_moderator=request.user)
        # Con "many" indicamos que reports es una lista y no un solo objeto
        serializer = self.get_serializer(reports, many=True)
        return Response(serializer.data)
    
    """ Permite al moderador autenticado asignarse un reporte a sí mismo """

    # Asignamos true en "detail" ya que requiere un ID de reporte (pk) en la URL
    # Este endpoint solo acepta solicitudes POST
    @action(detail=True, methods=['post'])
    # pk=None → Parámetro que recibirá el ID del reporte desde la URL.
    def assign_to_me(self, request, pk=None, url_path='assign'):
        # Obtiene la instancia del Report cuyo ID fue pasado en la URL
        report = self.get_object()
        # Verifica si el reporte ya tiene un usuario asignado
        if report.assigned_moderator is not None:
            return Response({'detail': 'This report is already assigned.'}, status=status.HTTP_400_BAD_REQUEST)

        report.assigned_moderator = request.user
        report.save()

        return Response({'detail': 'Report assigned successfully.'}, status=status.HTTP_200_OK)
    
    """ Actualiza el estado de un reporte específico a 'In Progress', 'Resolved' o 'Rejected' mediante una solicitud POST """
    
    @action(detail=True, methods=['post'], url_path='change_status')
    def change_status(self, request, pk=None):
        report = self.get_object()
        # Obtiene desde el cuerpo de la solicitud POST el nuevo estado que se quiere asignar
        new_status_name = request.data.get('status')

        if new_status_name not in ['In Progress', 'Resolved', 'Rejected']:
            return Response({'detail': 'Invalid status.'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            # Busca en la tabla ReportStatus un registro cuyo campo name coincida con new_status_name
            new_status = ReportStatus.objects.get(name=new_status_name)
        except ReportStatus.DoesNotExist:
            return Response({'detail': 'Status does not exist in the system.'}, status=status.HTTP_404_NOT_FOUND)

        report.status = new_status
        report.save()
        return Response({'detail': f'Status updated to {new_status_name}.'}, status=status.HTTP_200_OK)
    
    """ Permite a usuarios no autenticados ver solo los reportes aprobados (En progreso) """
    
    # No requiere autenticación, es público. Por lo tanto, dejamos vacio "permission_classes"
    @action(detail=False, methods=['get'], permission_classes=[], url_path='approved')
    def list_approved(self, request):
        # El doble guion bajo indica que estamos filtrando por un campo de la tabla relacionada (status.name)
        approved_reports = Report.objects.filter(status__name='In Progress')
        serializer = self.get_serializer(approved_reports, many=True)
        return Response(serializer.data)

    """ Permite a usuarios no autenticados crear un reporte desde la parte pública """
    
    # Usamos AllowAny ya que Cualquier persona sin autenticación puede usarlo
    @action(detail=False, methods=['post'], permission_classes=[AllowAny], url_path='public-create')
    def public_create(self, request):
        # Crea una instancia del serializer (PublicReportSerializer) con los datos que el usuario envió
        serializer = PublicReportSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'detail': 'Report created successfully.'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ReportStatusViewSet(viewsets.ModelViewSet):
    queryset = ReportStatus.objects.all()
    serializer_class = ReportStatusSerializer

class ReportSeverityViewSet(viewsets.ModelViewSet):
    queryset = ReportSeverity.objects.all()
    serializer_class = ReportSeveritySerializer

class CityViewSet(viewsets.ModelViewSet):
    queryset = City.objects.all()
    serializer_class = CitySerializer

class ProvinceViewSet(viewsets.ModelViewSet):
    queryset = Province.objects.all()
    serializer_class = ProvinceSerializer
