from django.db import models

# Create your models here.
from datetime import datetime

from django.contrib.auth.models import User
from django.db import models

# Create your models here.

 # BD de puntos fijos
class PuntosFijos(models.Model):
    nombre = models.CharField(max_length=300, blank=True, null=True)
    numero_de_chaleco = models.CharField(max_length=10, blank=True, null=True)
    direccion = models.CharField(max_length=300, blank=True, null=True)
    hora_de_ingreso = models.CharField(max_length=300, blank=True, null=True)
    hora_de_salida = models.CharField(max_length=300, blank=True, null=True)
    novedad = models.CharField(max_length=300, blank=True, null=True)
    fecha_de_creacion = models.DateTimeField(default=datetime.now, blank=True)
    #resgistro_fotografico = models.ImageField(upload_to='registros', blank=True)

    def __str__(self):
        return self.nombre

 # BD de institucion
class Institucion(models.Model):
    nombre = models.CharField(max_length=100, blank=True, null=True)
    fecha_de_creacion = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.nombre

 # BD de corredores
class Corredor(models.Model):
    nombre_del_corredor = models.CharField(max_length=100, blank=True, null=True)
    tipo_de_corredor = models.ForeignKey('TipoDeCorredor', on_delete=models.CASCADE, blank=True)
    encargado = models.ForeignKey(User, on_delete=models.CASCADE, blank=True)
    institucion = models.ForeignKey('Institucion', on_delete=models.CASCADE, blank=True)
    puntos = models.ManyToManyField(PuntosFijos, blank=True)
    fecha_de_creacion = models.DateField(blank=True)
    direccion = models.CharField(max_length=300, blank=True, null=True)
    hora_de_ingreso = models.TimeField(blank=True, null=True)
    hora_de_salida = models.TimeField(blank=True, null=True)

    def __str__(self):
        return str(self.tipo_de_corredor)

# BD del tipo de corredor
class TipoDeCorredor(models.Model):
    nombre = models.CharField(max_length=100, blank=True, null=True)
    fecha_de_creacion = models.DateField(blank=True, null=True)
    activo = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre

 # BD de imagenes
class Images(models.Model):
    nombre = models.CharField(max_length=100, blank=True, null=True)
    imagen = models.ImageField(upload_to='imagen', blank=True)

    def __str__(self):
        return self.nombre