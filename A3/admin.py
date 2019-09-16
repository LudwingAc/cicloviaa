from django.contrib import admin

# Register your models here.
from A3.models import PuntosFijos, Institucion, Corredor, Images, TipoDeCorredor, EventosRealizados, \
    ActivacionesYProyectosRealizados, UnidadesDeApoyo, AccidentesOcurridos, Eps, UnidadesSolicitadasOtrasInst

admin.site.site_header="Administrador Ciclovia"
admin.site.site_title="Ciclovia"
admin.site.index_title="Administrador"
admin.site.register(PuntosFijos)
admin.site.register(Institucion)
admin.site.register(Corredor)
admin.site.register(Images)
admin.site.register(TipoDeCorredor)
admin.site.register(EventosRealizados)
admin.site.register(ActivacionesYProyectosRealizados)
admin.site.register(UnidadesDeApoyo)
admin.site.register(AccidentesOcurridos)
admin.site.register(Eps)
admin.site.register(UnidadesSolicitadasOtrasInst)
