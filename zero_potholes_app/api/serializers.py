"""
Serializers:
Convierten modelos Django ↔ JSON para comunicación vía API.
"""

from rest_framework import serializers
from zero_potholes_app.models import (
    Report,
    ReportStatus,
    ReportSeverity,
    City,
    Province,
)


class PublicReportSerializer(serializers.ModelSerializer):
    """
    Serializer para creación pública de reportes sin autenticación.
    Solo expone los campos estrictamente necesarios.
    """

    class Meta:
        model = Report
        fields = [
            "citizen_first_name",
            "citizen_last_name",
            "citizen_email",
            "latitude",
            "longitude",
            "street_name",
            "street_number",
            "city",
            "image",
            "description",
        ]

    def validate(self, data):
        """
        Evita duplicados:
        No se permite más de un reporte en una misma ubicación
        con descripción similar dentro de un radio razonable.
        """
        lat = data.get("latitude")
        lon = data.get("longitude")

        exists = Report.objects.filter(
            latitude__range=(lat - 0.0001, lat + 0.0001),
            longitude__range=(lon - 0.0001, lon + 0.0001),
        ).exists()

        if exists:
            raise serializers.ValidationError(
                "Ya existe un reporte registrado en esta ubicación."
            )

        return data

    def create(self, validated_data):
        """
        Asigna automáticamente el estado inicial 'Received'.
        """
        status_received = ReportStatus.objects.get(name="Received")
        return Report.objects.create(status=status_received, **validated_data)


class ReportSerializer(serializers.ModelSerializer):
    """
    Serializer completo para moderadores y administradores.
    """

    class Meta:
        model = Report
        fields = "__all__"
        extra_kwargs = {
            "severity": {"required": False, "allow_null": True},
            "assigned_moderator": {"required": False, "allow_null": True},
        }


class ReportStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReportStatus
        fields = "__all__"


class ReportSeveritySerializer(serializers.ModelSerializer):
    class Meta:
        model = ReportSeverity
        fields = "__all__"


class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = "__all__"


class ProvinceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Province
        fields = "__all__"
