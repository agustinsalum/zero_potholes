"""

Converts database models into a format (usually JSON) that the API can send or receive.

"""


from rest_framework import serializers
from zero_potholes_app.models import Report

class ReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Report
        fields = '__all__'
