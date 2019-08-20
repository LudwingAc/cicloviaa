import datetime

import psycopg2
from django.shortcuts import render
import sqlite3

# Create your views here.
def addpf(request):
    now = datetime.datetime.now()

    now = now = now.astimezone()

    con = psycopg2.connect(
        "host='ec2-184-73-169-163.compute-1.amazonaws.com' dbname='d9ir03ok1rn1j8' user='rumtiwmezjfhkm' password='83ebef2592e91bc65b39f5e61e54e85cc1150546a0e463f4d55f53ca5e2a84ff'")
    cur = con.cursor()

    cur.execute('SELECT ins.nombre, pf.direccion, pf.nombre, pf.hora_de_ingreso, pf.hora_de_salida, pf.numero_de_chaleco, pf.novedad FROM "A3_corredor" AS co, "A3_institucion" AS ins , "A3_corredor_puntos" AS cp, "A3_puntosfijos" AS pf WHERE ins.id = co.institucion_id AND cp.corredor_id = co.id AND pf.id = cp.puntosfijos_id');
    c1 = cur.fetchall()

    # conn = sqlite3.connect('db.sqlite3')
    # c = conn.cursor()  # The database will be saved in the location where your 'py' file is saved
    #
    # #SELECT ins.cedula, ins.nombres, ins.apellidos, ins.cedula, ins.correo, ins.telefono
    # # FROM nn_inscripcion AS ins INNER JOIN nn_taller AS taller ON ins.taller_id = taller.id
    #
    # # Create table - CLIENTS
    # c.execute("SELECT ins.nombre, pf.direccion, pf.nombre, pf.hora_de_ingreso, pf.hora_de_salida, pf.numero_de_chaleco, pf.novedad "
    #           "FROM A3_Corredor AS co "
    #           "INNER JOIN A3_Institucion AS ins ON co.institucion_id = ins.id "
    #           "INNER JOIN A3_corredor_puntos AS cp ON co.id = cp.corredor_id "
    #           "INNER JOIN A3_PuntosFijos AS pf ON cp.puntosfijos_id = pf.id")
    # c1 = c.fetchall()

    cur.execute('SELECT co.id, co.nombre_del_corredor, co.fecha_de_creacion, us.first_name, us.last_name, co.direccion, co.hora_de_ingreso, co.hora_de_salida FROM "A3_corredor" AS co INNER JOIN "auth_user" AS us ON us.id = co.encargado_id;')
    corredor = cur.fetchall()

    cur.execute('SELECT * FROM "A3_images" ;')
    imagenes = cur.fetchall()

    return render(request, 'addPuntosFijos.html', {'data':c1, 'now':now, 'corredor':corredor, 'imagenes':imagenes})