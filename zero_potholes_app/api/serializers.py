
"""

Convierte los modelos de base de datos en un formato (usualmente JSON) que la API puede enviar o recibir.

"""


from rest_framework import serializers
from zero_potholes_app.models import Report, ReportStatus, ReportSeverity, City, Province

class PublicReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Report
        # Incluimos solamente algunos campos
        fields = [
            'citizen_first_name',
            'citizen_last_name',
            'citizen_email',
            'latitude',
            'longitude',
            'street_name',
            'street_number',
            'city',
            'image',
            'description',
        ]

    def create(self, validated_data):
        # Asigna automáticamente el estado 'Received' al crear la denuncia pública
        status_received = ReportStatus.objects.get(name='Received')
        return Report.objects.create(status=status_received, **validated_data)

class ReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Report
        fields = '__all__'
        # El campo "severity" se omite al crear la denuncia, tanto en el formulario como en la base de datos
        extra_kwargs = {
            'severity': {'required': False, 'allow_null': True}
        }

class ReportStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReportStatus
        fields = '__all__'

class ReportSeveritySerializer(serializers.ModelSerializer):
    class Meta:
        model = ReportSeverity
        fields = '__all__'

class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = '__all__'

class ProvinceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Province
        fields = '__all__'
