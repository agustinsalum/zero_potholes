
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

    """ Allows the authenticated user to list their assigned reports """

    @action(detail=False, methods=['get'], url_path='assigned')
    def assigned_to_me(self, request):
        reports = Report.objects.filter(user=request.user)
        serializer = self.get_serializer(reports, many=True)
        return Response(serializer.data)
    
    """ Allows the authenticated moderator to assign a report to themselves """

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
    
    """  Updates the status of a specific report to in_progress, resolved, or rejected using a POST request """
    
    @action(detail=True, methods=['post'], url_path='change_status')
    def change_status(self, request, pk=None):
        report = self.get_object()
        # Extracts the new status from the request body (JSON)
        new_status_name = request.data.get('status')

        if new_status_name not in ['In Progress', 'Resolved']:
            return Response({'detail': 'Invalid status.'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            # Fetches the ReportStatus object from the database where the name field matches the value of new_status_name.
            new_status = ReportStatus.objects.get(name=new_status_name)
        except ReportStatus.DoesNotExist:
            return Response({'detail': 'Status does not exist in the system.'}, status=status.HTTP_404_NOT_FOUND)

        report.status = new_status
        report.save()
        return Response({'detail': f'Status updated to {new_status_name}.'}, status=status.HTTP_200_OK)


class ReportStatusViewSet(viewsets.ModelViewSet):
    queryset = ReportStatus.objects.all()
    serializer_class = ReportStatusSerializer

class CityViewSet(viewsets.ModelViewSet):
    queryset = City.objects.all()
    serializer_class = CitySerializer

class ProvinceViewSet(viewsets.ModelViewSet):
    queryset = Province.objects.all()
    serializer_class = ProvinceSerializer
