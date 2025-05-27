
"""

Defines the views that manage the logic for CRUD operations on the models.

"""

from rest_framework import viewsets

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

    @action(detail=False, methods=['get'], url_path='assigned')
    def assigned_to_me(self, request):
        reports = Report.objects.filter(user=request.user)
        serializer = self.get_serializer(reports, many=True)
        return Response(serializer.data)

class ReportStatusViewSet(viewsets.ModelViewSet):
    queryset = ReportStatus.objects.all()
    serializer_class = ReportStatusSerializer

class CityViewSet(viewsets.ModelViewSet):
    queryset = City.objects.all()
    serializer_class = CitySerializer

class ProvinceViewSet(viewsets.ModelViewSet):
    queryset = Province.objects.all()
    serializer_class = ProvinceSerializer
