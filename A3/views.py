import datetime

from django.shortcuts import render
import sqlite3

# Create your views here.
def addpf(request):
    now = datetime.datetime.now()

    now = now = now.astimezone()

    conn = sqlite3.connect('db.sqlite3')
    c = conn.cursor()  # The database will be saved in the location where your 'py' file is saved

    #SELECT ins.cedula, ins.nombres, ins.apellidos, ins.cedula, ins.correo, ins.telefono
    # FROM nn_inscripcion AS ins INNER JOIN nn_taller AS taller ON ins.taller_id = taller.id

    # Create table - CLIENTS
    c.execute("SELECT ins.nombre, pf.direccion, pf.nombre, pf.hora_de_ingreso, pf.hora_de_salida, pf.numero_de_chaleco, pf.novedad "
              "FROM A3_Corredor AS co "
              "INNER JOIN A3_Institucion AS ins ON co.institucion_id = ins.id "
              "INNER JOIN A3_corredor_puntos AS cp ON co.id = cp.corredor_id "
              "INNER JOIN A3_PuntosFijos AS pf ON cp.puntosfijos_id = pf.id")
    c1 = c.fetchall()

    c.execute("SELECT co.id, co.nombre_del_corredor, co.fecha_de_creacion, us.first_name, us.last_name, co.direccion FROM A3_Corredor AS co INNER JOIN auth_user AS us ON us.id = co.encargado_id")
    corredor = c.fetchall()

    return render(request, 'addPuntosFijos.html', {'data':c1, 'now':now, 'corredor':corredor})