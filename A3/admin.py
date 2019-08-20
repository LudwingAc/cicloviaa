from django.contrib import admin

# Register your models here.
from A3.models import PuntosFijos, Institucion, Corredor, Images

admin.site.register(PuntosFijos)
admin.site.register(Institucion)
admin.site.register(Corredor)
admin.site.register(Images)