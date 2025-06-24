"""

Converts database models into a format (usually JSON) that the API can send or receive.

"""


from rest_framework import serializers
from zero_potholes_app.models import Report, ReportStatus, ReportSeverity, City, Province

class ReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Report
        fields = '__all__'
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
