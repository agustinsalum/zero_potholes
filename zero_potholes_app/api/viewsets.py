"""
ViewSets:
Contienen la lógica de negocio y operaciones CRUD expuestas por la API.
"""

from django.db import transaction
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated

from zero_potholes_app.models import (
    Report,
    ReportStatus,
    ReportSeverity,
    City,
    Province,
)
from zero_potholes_app.api.serializers import (
    PublicReportSerializer,
    ReportSerializer,
    ReportStatusSerializer,
    ReportSeveritySerializer,
    CitySerializer,
    ProvinceSerializer,
)


# -------------------------------------------------------------------
#                             REPORTES
# -------------------------------------------------------------------

class ReportViewSet(viewsets.ModelViewSet):
    """
    ViewSet principal para gestión de reportes.
    Incluye endpoints públicos y privados.
    """

    queryset = Report.objects.select_related(
        "city", "status", "severity", "assigned_moderator"
    ).all()
    serializer_class = ReportSerializer
    permission_classes = [IsAuthenticated]

    # -----------------------------
    # ENDPOINTS PRIVADOS
    # -----------------------------

    @action(detail=False, methods=["get"], url_path="assigned")
    def assigned_to_me(self, request):
        """
        Lista los reportes asignados al moderador autenticado.
        """
        reports = self.queryset.filter(assigned_moderator=request.user)
        serializer = self.get_serializer(reports, many=True)
        return Response(serializer.data)

    @action(detail=True, methods=["post"], url_path="assign")
    def assign_to_me(self, request, pk=None):
        """
        Permite al moderador asignarse un reporte a sí mismo.
        La operación es atómica para evitar colisiones.
        """
        with transaction.atomic():
            report = Report.objects.select_for_update().get(pk=pk)

            if report.assigned_moderator is not None:
                return Response(
                    {"detail": "This report is already assigned."},
                    status=status.HTTP_400_BAD_REQUEST,
                )

            report.assigned_moderator = request.user
            report.save()

        return Response(
            {"detail": "Report assigned successfully."},
            status=status.HTTP_200_OK,
        )

    @action(detail=True, methods=["post"], url_path="change_status")
    def change_status(self, request, pk=None):
        """
        Cambia el estado de un reporte.
        Estados permitidos:
        - In Progress
        - Resolved
        - Rejected
        """
        report = self.get_object()
        new_status_name = request.data.get("status")

        allowed_transitions = {
            "Received": ["In Progress", "Rejected"],
            "In Progress": ["Resolved", "Rejected"],
        }

        current_status = report.status.name

        if (
            current_status not in allowed_transitions
            or new_status_name not in allowed_transitions[current_status]
        ):
            return Response(
                {"detail": "Invalid status transition."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        try:
            new_status = ReportStatus.objects.get(name=new_status_name)
        except ReportStatus.DoesNotExist:
            return Response(
                {"detail": "Status does not exist in the system."},
                status=status.HTTP_404_NOT_FOUND,
            )

        report.status = new_status
        report.save()

        return Response(
            {"detail": f"Status updated to {new_status_name}."},
            status=status.HTTP_200_OK,
        )

    # -----------------------------
    # ENDPOINTS PÚBLICOS
    # -----------------------------

    @action(
        detail=False,
        methods=["get"],
        permission_classes=[AllowAny],
        url_path="approved",
    )
    def list_approved(self, request):
        """
        Devuelve los reportes visibles al público (estado: In Progress).
        """
        approved_reports = self.queryset.filter(status__name="In Progress")
        serializer = self.get_serializer(approved_reports, many=True)
        return Response(serializer.data)

    @action(
        detail=False,
        methods=["post"],
        permission_classes=[AllowAny],
        url_path="public-create",
    )
    def public_create(self, request):
        """
        Permite a usuarios no autenticados crear un reporte público.
        """
        serializer = PublicReportSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {"detail": "Report created successfully."},
                status=status.HTTP_201_CREATED,
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# -------------------------------------------------------------------
#                          VIEWSETS DE CATÁLOGO
# -------------------------------------------------------------------

class ReportStatusViewSet(viewsets.ModelViewSet):
    queryset = ReportStatus.objects.all()
    serializer_class = ReportStatusSerializer


class ReportSeverityViewSet(viewsets.ModelViewSet):
    queryset = ReportSeverity.objects.all()
    serializer_class = ReportSeveritySerializer


class CityViewSet(viewsets.ModelViewSet):
    queryset = City.objects.select_related("province").all()
    serializer_class = CitySerializer


class ProvinceViewSet(viewsets.ModelViewSet):
    queryset = Province.objects.all()
    serializer_class = ProvinceSerializer
