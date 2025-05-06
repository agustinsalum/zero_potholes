from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Province(models.Model):
    name = models.CharField(max_length=100, primary_key=True)

    def __str__(self):
        return self.name

class City(models.Model):
    name = models.CharField(max_length=100, primary_key=True)
    province = models.ForeignKey(Province, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name}, {self.province.name}"

class ReportStatus(models.Model):
    name = models.CharField(max_length=20, primary_key=True)

    def __str__(self):
        return self.name

class Report(models.Model):
    id = models.AutoField(primary_key=True)
    image = models.ImageField(upload_to='reports/')
    description = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)
    street_name = models.CharField(max_length=100)
    street_number = models.CharField(max_length=10)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    status = models.ForeignKey(ReportStatus, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"Report #{self.id} - {self.status.name}"
