from django.contrib import admin
from .models import Province, City, ReportStatus, Report, ReportSeverity


@admin.register(Province)
class ProvinceAdmin(admin.ModelAdmin):
    list_display = ("id", "name")
    search_fields = ("name",)


@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "province")
    list_filter = ("province",)
    search_fields = ("name",)


@admin.register(ReportStatus)
class ReportStatusAdmin(admin.ModelAdmin):
    list_display = ("name",)


@admin.register(ReportSeverity)
class ReportSeverityAdmin(admin.ModelAdmin):
    list_display = ("name",)


@admin.register(Report)
class ReportAdmin(admin.ModelAdmin):
    list_display = ("id", "status", "severity", "city", "assigned_moderator", "date")
    list_filter = ("status", "severity", "city", "assigned_moderator")
    search_fields = ("street_name", "citizen_email")
    readonly_fields = ("date",)
