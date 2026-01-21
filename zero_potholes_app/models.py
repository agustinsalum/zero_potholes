from django.db import models
from django.contrib.auth.models import User


# -------------------------------------------------------------------
#                           MODELOS GEOGRÁFICOS
# -------------------------------------------------------------------

class Province(models.Model):
    """
    Representa una provincia.
    """
    name = models.CharField(max_length=100, unique=True)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name


class City(models.Model):
    """
    Representa una ciudad perteneciente a una provincia.
    """
    name = models.CharField(max_length=100)
    province = models.ForeignKey(
        Province,
        on_delete=models.CASCADE,
        related_name="cities"
    )

    class Meta:
        unique_together = ("name", "province")
        ordering = ["name"]

    def __str__(self):
        return f"{self.name}, {self.province.name}"


# -------------------------------------------------------------------
#                         MODELOS DE CATÁLOGO
# -------------------------------------------------------------------

class ReportStatus(models.Model):
    """
    Estado del reporte:
    - Received
    - In Progress
    - Resolved
    - Rejected
    """
    name = models.CharField(max_length=20, primary_key=True)

    def __str__(self):
        return self.name


class ReportSeverity(models.Model):
    """
    Nivel de gravedad:
    - Very Low
    - Low
    - Moderate
    - High
    - Critical
    """
    name = models.CharField(max_length=20, primary_key=True)

    def __str__(self):
        return self.name


# -------------------------------------------------------------------
#                             MODELO PRINCIPAL
# -------------------------------------------------------------------

class Report(models.Model):
    """
    Denuncia realizada por un ciudadano sobre un bache o imperfección vial.
    """

    # Imagen del problema reportado
    image = models.ImageField(upload_to="reports/")

    # Descripción textual del incidente
    description = models.TextField()

    # Fecha y hora de creación automática
    date = models.DateTimeField(auto_now_add=True)

    # Datos del ciudadano
    citizen_first_name = models.CharField(max_length=50)
    citizen_last_name = models.CharField(max_length=50)
    citizen_email = models.EmailField()

    # Coordenadas geográficas del incidente
    latitude = models.FloatField()
    longitude = models.FloatField()

    # Dirección textual (opcional)
    street_name = models.CharField(max_length=100, null=True, blank=True)
    street_number = models.CharField(max_length=10, null=True, blank=True)
    street_height = models.IntegerField(null=True, blank=True)

    # Relaciones
    city = models.ForeignKey(
        City,
        on_delete=models.CASCADE,
        related_name="reports"
    )

    status = models.ForeignKey(
        ReportStatus,
        on_delete=models.CASCADE,
        related_name="reports"
    )

    # La gravedad se asigna por un moderador (opcional)
    severity = models.ForeignKey(
        ReportSeverity,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="reports"
    )

    # Moderador asignado al caso
    assigned_moderator = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="assigned_reports"
    )

    class Meta:
        ordering = ["-date"]

    def __str__(self):
        return f"Reporte #{self.id} - {self.status.name}"
