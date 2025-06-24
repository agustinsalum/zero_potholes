from django.contrib import admin

from .models import Province, City, ReportStatus, Report, ReportSeverity

# Register your models here.

admin.site.register(Province)
admin.site.register(City)
admin.site.register(ReportStatus)
admin.site.register(Report)
admin.site.register(ReportSeverity)