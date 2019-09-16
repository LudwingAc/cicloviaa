from django.db import models

# Create your models here.
from datetime import datetime

from django.contrib.auth.models import User
from django.db import models

# Create your models here.

 # BD de puntos fijos
class Guardianes(models.Model):
    nombre = models.CharField(max_length=300, blank=True, null=True)
    numero_de_contrato = models.CharField(max_length=10, blank=True, null=True)
    numero_de_contacto = models.CharField(max_length=15, blank=True, null=True)
    direccion = models.CharField(max_length=300, blank=True, null=True)
    asistio = models.BooleanField(default=False)
    inasistio = models.BooleanField(default=False)
    retardo = models.BooleanField(default=False)
    devolucion = models.BooleanField(default=False)
    acciones_tomadas = models.CharField(max_length=300, blank=True, null=True)
    novedad = models.TextField(blank=True)
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

class EventosRealizados(models.Model):
    evento = models.CharField(max_length=200, blank=True, null=True)
    ubicacion = models.CharField(max_length=200, blank=True, null=True)
    organizador = models.CharField(max_length=200, blank=True, null=True)
    hora_de_inicio = models.TimeField(blank=True, null=True)
    hora_de_final = models.TimeField(blank=True, null=True)
    observaciones = models.TextField(blank=True)

    def __str__(self):
        return str(self.evento)

class ActivacionesYProyectosRealizados(models.Model):
    evento = models.CharField(max_length=200, blank=True, null=True)
    ubicacion = models.CharField(max_length=200, blank=True, null=True)
    organizador = models.CharField(max_length=200, blank=True, null=True)
    hora_de_inicio = models.TimeField(blank=True, null=True)
    hora_de_final = models.TimeField(blank=True, null=True)
    observaciones = models.TextField(blank=True)

    def __str__(self):
        return str(self.evento)


class UnidadesDeApoyo(models.Model):
    institucion_o_alianza = models.CharField(max_length=200, blank=True, null=True)
    lugar_de_ubicacion = models.CharField(max_length=200, blank=True, null=True)
    nombre_del_apoyo = models.CharField(max_length=200, blank=True, null=True)
    hora_de_llegada = models.TimeField(blank=True, null=True)
    hora_de_retiro = models.TimeField(blank=True, null=True)
    numeral_de_la_unidad_CPS = models.CharField(max_length=200, blank=True, null=True)
    novedades_presentadas = models.TextField(blank=True)

    def __str__(self):
        return str(self.institucion_o_alianza)

class UnidadesSolicitadasOtrasInst(models.Model):
    lugar = models.CharField(max_length=200, blank=True, null=True)
    novedad = models.CharField(max_length=200, blank=True, null=True)
    guardia_que_solicita = models.CharField(max_length=200, blank=True, null=True)
    hora_de_solicitud = models.TimeField(blank=True, null=True)
    hora_de_atencion = models.TimeField(blank=True, null=True)
    numeral_unidad = models.CharField(max_length=200, blank=True, null=True)
    n_movil_o_placa = models.CharField(max_length=200, blank=True, null=True)
    hora_finalizacion = models.TimeField(blank=True, null=True)
    accion_final = models.TextField(blank=True)

    def __str__(self):
        return str(self.lugar)

class AccidentesOcurridos(models.Model):
    hora_de_inicio = models.TimeField(blank=True, null=True)
    lugar = models.CharField(max_length=200, blank=True, null=True)
    ruta = models.CharField(max_length=200, blank=True, null=True)
    nombre_del_atendido = models.CharField(max_length=200, blank=True, null=True)
    cc_o_ti_del_atendido = models.CharField(max_length=200, blank=True, null=True)
    GENDER_CHOICES = (
        ('Hombre', 'Hombre'),
        ('Mujer', 'Mujer'),
        ('NA', 'NA'),
    )
    genero_atendido = models.CharField(max_length=10, choices=GENDER_CHOICES)
    edad = models.CharField(max_length=3,blank=True, null=True)
    eps_atendido = models.ForeignKey('Eps', on_delete=models.CASCADE, blank=True, null=True)
    telefono_atendido = models.CharField(max_length=15,blank=True, null=True)
    diagnostico = models.TextField(blank=True)
    causa = models.CharField(max_length=200, blank=True, null=True)
    accion_final = models.CharField(max_length=200, blank=True, null=True)
    unidad_que_realiza_la_atencion = models.CharField(max_length=200, blank=True, null=True)
    hora_de_final = models.TimeField(blank=True, null=True)

    def __str__(self):
        return str(self.lugar)

class Eps(models.Model):
    nombre = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return str(self.nombre)

# BD del tipo de corredor
class TipoDeCorredor(models.Model):
    nombre = models.CharField(max_length=100, blank=True, null=True)
    fecha_de_creacion = models.DateField(blank=True, null=True)
    activo = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre


 # BD de corredores
class Corredor(models.Model):
    tipo_de_corredor = models.ForeignKey('TipoDeCorredor', on_delete=models.CASCADE, blank=True)
    encargado = models.ForeignKey(User, on_delete=models.CASCADE, blank=True)
    institucion = models.ForeignKey('Institucion', on_delete=models.CASCADE, blank=True)
    guardianes = models.ManyToManyField(Guardianes, blank=True)
    fecha_de_creacion = models.DateField(blank=True)
    direccion = models.CharField(max_length=300, blank=True, null=True)
    hora_de_ingreso = models.TimeField(blank=True, null=True)
    hora_de_salida = models.TimeField(blank=True, null=True)
    desarrollo_de_la_jornada = models.TextField(blank=True)
    solicitudes = models.TextField(blank=True)
    eventos_realizados = models.ManyToManyField(EventosRealizados, blank=True)
    activaciones = models.ManyToManyField(ActivacionesYProyectosRealizados, blank=True)
    unidades_de_apoyo = models.ManyToManyField(UnidadesDeApoyo, blank=True)
    accidentes_ocurridos = models.ManyToManyField(AccidentesOcurridos, blank=True)
    unidades_solicitada_otras_inst = models.ManyToManyField(UnidadesSolicitadasOtrasInst, blank=True)

    def __str__(self):
        return str(self.tipo_de_corredor)


 # BD de imagenes
class Images(models.Model):
    nombre = models.CharField(max_length=100, blank=True, null=True)
    imagen = models.ImageField(upload_to='imagen', blank=True)

    def __str__(self):
        return self.nombre