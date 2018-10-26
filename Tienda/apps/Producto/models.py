from django.db import models

class Producto(models.Model):
    nombreProducto = models.CharField(max_length=30)
    descripcion = models.CharField(max_length=50)
    costo = models.DecimalField(max_digits=6,decimal_places=2)
    disponible = models.NullBooleanField()
    numExistencias = models.IntegerField(default=0)