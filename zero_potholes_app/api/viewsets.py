
"""

Defines the views that manage the logic for CRUD operations on the models.

"""

from rest_framework import viewsets, status

from rest_framework.decorators import action
from rest_framework.response import Response


from zero_potholes_app.models import Report, ReportStatus, City, Province
from zero_potholes_app.api.serializers import (
    ReportSerializer,
    ReportStatusSerializer,
    CitySerializer,
    ProvinceSerializer
)

class ReportViewSet(viewsets.ModelViewSet):
    queryset = Report.objects.all()
    serializer_class = ReportSerializer

    # Allows the authenticated user to list their assigned reports
    @action(detail=False, methods=['get'], url_path='assigned')
    def assigned_to_me(self, request):
        reports = Report.objects.filter(user=request.user)
        serializer = self.get_serializer(reports, many=True)
        return Response(serializer.data)
    
    # Allows the authenticated moderator to assign a report to themselves
    # PK should be None; "detail=True" means the action operates on a specific instance (requires an object in the URL)
    # detail=True because this action works with a specific report
    @action(detail=True, methods=['post'])
    def assign_to_me(self, request, pk=None):
        # Gets the Report instance whose ID was passed in the URL
        report = self.get_object()
        
        # Checks if the report already has an assigned user
        if report.user is not None:
            return Response({'detail': 'This report is already assigned.'}, status=status.HTTP_400_BAD_REQUEST)

        report.user = request.user
        report.save()

        return Response({'detail': 'Report assigned successfully.'}, status=status.HTTP_200_OK)


class ReportStatusViewSet(viewsets.ModelViewSet):
    queryset = ReportStatus.objects.all()
    serializer_class = ReportStatusSerializer

class CityViewSet(viewsets.ModelViewSet):
    queryset = City.objects.all()
    serializer_class = CitySerializer

class ProvinceViewSet(viewsets.ModelViewSet):
    queryset = Province.objects.all()
    serializer_class = ProvinceSerializer
