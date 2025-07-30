
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
        reports = Report.objects.filter(user=request.user)
        serializer = self.get_serializer(reports, many=True)
        return Response(serializer.data)
    
    """ Permite al moderador autenticado asignarse un reporte a sí mismo """

    # PK debería ser None; "detail=True" significa que la acción opera sobre una instancia específica (requiere un objeto en la URL)
    # detail=True porque esta acción trabaja con un reporte específico
    @action(detail=True, methods=['post'])
    def assign_to_me(self, request, pk=None, url_path='assign'):
        # Obtiene la instancia del Report cuyo ID fue pasado en la URL
        report = self.get_object()
        
        # Cerifica si el reporte ya tiene un usuario asignado
        if report.user is not None:
            return Response({'detail': 'This report is already assigned.'}, status=status.HTTP_400_BAD_REQUEST)

        report.user = request.user
        report.save()

        return Response({'detail': 'Report assigned successfully.'}, status=status.HTTP_200_OK)
    
    """ Actualiza el estado de un reporte específico a 'In Progress', 'Resolved' o 'Rejected' mediante una solicitud POST """
    
    @action(detail=True, methods=['post'], url_path='change_status')
    def change_status(self, request, pk=None):
        report = self.get_object()
        # Extrae el nuevo estado desde el cuerpo de la solicitud (JSON)
        new_status_name = request.data.get('status')

        if new_status_name not in ['In Progress', 'Resolved', 'Rejected']:
            return Response({'detail': 'Invalid status.'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            # Obtiene el objeto ReportStatus de la base de datos cuyo campo 'name' coincide con el valor de new_status_name
            new_status = ReportStatus.objects.get(name=new_status_name)
        except ReportStatus.DoesNotExist:
            return Response({'detail': 'Status does not exist in the system.'}, status=status.HTTP_404_NOT_FOUND)

        report.status = new_status
        report.save()
        return Response({'detail': f'Status updated to {new_status_name}.'}, status=status.HTTP_200_OK)
    
    """ Permite a usuarios no autenticados ver solo los reportes aprobados (En progreso) """
    
    @action(detail=False, methods=['get'], permission_classes=[], url_path='approved')
    def list_approved(self, request):
        approved_reports = Report.objects.filter(status__name='In Progress')
        serializer = self.get_serializer(approved_reports, many=True)
        return Response(serializer.data)
    
    @action(detail=False, methods=['post'], permission_classes=[AllowAny], url_path='public-create')
    def public_create(self, request):
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
