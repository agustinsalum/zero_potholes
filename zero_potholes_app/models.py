from django.db import models
from django.contrib.auth.models import User

# Crea tus modelos aquí

class Province(models.Model):
    name = models.CharField(max_length=100, primary_key=True)

    # Mostrar la instancia del modelo cuando se convierte a string
    def __str__(self):
        return self.name

class City(models.Model):
    name = models.CharField(max_length=100, primary_key=True)
    province = models.ForeignKey(Province, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name}, {self.province.name}"

class ReportStatus(models.Model):
    # Estados: "Received", "In Progress", "Resolved" or "Rejected"
    name = models.CharField(max_length=20, primary_key=True)

    def __str__(self):
        return self.name
    
class ReportSeverity(models.Model):
    # Estados: Very low, Low, Moderate, High or Critical
    name = models.CharField(max_length=20, primary_key=True)

    def __str__(self):
        return self.name

class Report(models.Model):
    id = models.AutoField(primary_key=True)
    image = models.ImageField(upload_to='reports/')
    description = models.TextField()
    # Con "auto_now_add" asignamos automaticamente la fecha y hora
    date = models.DateTimeField(auto_now_add=True)
    citizen_first_name = models.CharField(max_length=50)
    citizen_last_name = models.CharField(max_length=50)
    citizen_email = models.EmailField()
    # Latitud y Longitud están entre -180 y 180
    # Con "max_digits" el total de dígitos que se pueden guardar es 9 (parte entera + decimales)
    # Con "decimal_places" de los 9 digitos permitimos 6 para la parte decimal (ej: 123.456789)
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)
    # Con "null" en la base de datos ese campo puede ser null
    # Con "black" en los formularios o validaciones puede quedar vacío (no es obligatorio)
    # Algunas ciudades utilizan números para identificar sus calles, mientras que otras nombres
    street_name = models.CharField(max_length=100, null=True, blank=True)
    street_number = models.CharField(max_length=10, null=True, blank=True)
    street_height = models.IntegerField(null=True, blank=True)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    status = models.ForeignKey(ReportStatus, on_delete=models.CASCADE)
    # La gravedad la asigna el moderador 
    severity = models.ForeignKey(ReportSeverity, on_delete=models.CASCADE, null=True, blank=True)
    # Con "SET_NULL" si el moderador es borrado, el campo assigned se pone NULL en lugar de borrar el Report
    assigned_moderator = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"Report #{self.id} - {self.status.name}"

