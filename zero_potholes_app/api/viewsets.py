
"""

Defines the views that manage the logic for CRUD operations on the models.

"""

from rest_framework import viewsets
from zero_potholes_app.models import Report
from zero_potholes_app.api.serializers import ReportSerializer

class ReportViewSet(viewsets.ModelViewSet):
    queryset = Report.objects.all()
    serializer_class = ReportSerializer
