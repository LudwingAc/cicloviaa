import datetime

import psycopg2
from django.shortcuts import render
import sqlite3

# Create your views here.
from A3.form import dateForm


def addpf(request, num):

    desde = ''
    hasta = ''

    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = dateForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            desde = form['f1'].value()
            hasta = form['f1'].value()
            print(desde)
            print(datetime.datetime.strptime(desde, "%Y-%m-%d").strftime("%d/%m/%Y"))

            #return render(request, 'col/res.html', {'respuesta': respuesta})

        # if a GET (or any other method) we'll create a blank form
    else:
        form = dateForm()

    now = datetime.datetime.now()

    now = now = now.astimezone()

    con = psycopg2.connect(
        "host='ec2-184-73-169-163.compute-1.amazonaws.com' dbname='d9ir03ok1rn1j8' user='rumtiwmezjfhkm' password='83ebef2592e91bc65b39f5e61e54e85cc1150546a0e463f4d55f53ca5e2a84ff'")
    cur = con.cursor()

    cur.execute('SELECT ins.nombre, pf.direccion, pf.nombre, pf.hora_de_ingreso, pf.hora_de_salida, pf.numero_de_chaleco, pf.novedad FROM "A3_corredor" AS co, "A3_institucion" AS ins , "A3_corredor_puntos" AS cp, "A3_puntosfijos" AS pf, "A3_tipodecorredor" AS tdp WHERE tdp.id=co.tipo_de_corredor_id and ins.id = co.institucion_id AND cp.corredor_id = co.id AND pf.id = cp.puntosfijos_id and co.tipo_de_corredor_id= %s and tdp.id=%s', (num, num));
    c1 = cur.fetchall()

    # if(desde!='' and hasta !=''):
    #     cur.execute('SELECT co.id, tdp.nombre, co.fecha_de_creacion, us.first_name, us.last_name, co.direccion, co.hora_de_ingreso, co.hora_de_salida FROM "A3_corredor" AS co INNER JOIN "auth_user" AS us ON us.id = co.encargado_id INNER JOIN "A3_tipodecorredor" AS tdp  ON tdp.id=co.tipo_de_corredor_id WHERE co.id= %s and co.id=%s and co.fecha_de_creacion = %s and co.fecha_de_creacion = %s', (num, num, desde, hasta))
    #     corredor = cur.fetchall()
    # else:
    cur.execute('SELECT co.id, tdp.nombre, co.fecha_de_creacion, us.first_name, us.last_name, co.direccion, co.hora_de_ingreso, co.hora_de_salida, tdp.id FROM "A3_corredor" AS co INNER JOIN "auth_user" AS us ON us.id = co.encargado_id INNER JOIN "A3_tipodecorredor" AS tdp  ON tdp.id=co.tipo_de_corredor_id WHERE co.tipo_de_corredor_id= %s and tdp.id=%s ',(num, num))
    corredor = cur.fetchall()

    cur.execute('SELECT co.id, tdp.nombre, co.fecha_de_creacion, us.first_name, us.last_name, co.direccion, co.hora_de_ingreso, co.hora_de_salida, tdp.id FROM "A3_corredor" AS co INNER JOIN "auth_user" AS us ON us.id = co.encargado_id INNER JOIN "A3_tipodecorredor" AS tdp  ON tdp.id=co.tipo_de_corredor_id ')
    filtro = cur.fetchall()

    cur.execute('SELECT tdp.id, tdp.nombre, tdp.fecha_de_creacion FROM "A3_tipodecorredor" AS tdp ;')
    corlista = cur.fetchall()

    cur.execute('SELECT * FROM "A3_images" ;')
    imagenes = cur.fetchall()

    return render(request, 'addPuntosFijos.html', {'form':form,'data':c1, 'now':now, 'corredor':corredor, 'imagenes':imagenes, 'listacorredor':corlista, 'filtro':filtro})

def general(request):

    desde = ''
    hasta = ''

    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = dateForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            desde = form['f1'].value()
            hasta = form['f1'].value()

        # if a GET (or any other method) we'll create a blank form
    else:
        form = dateForm()

    now = datetime.datetime.now()
    now = now = now.astimezone()
    con = psycopg2.connect(
        "host='ec2-184-73-169-163.compute-1.amazonaws.com' dbname='d9ir03ok1rn1j8' user='rumtiwmezjfhkm' password='83ebef2592e91bc65b39f5e61e54e85cc1150546a0e463f4d55f53ca5e2a84ff'")
    cur = con.cursor()

    cur.execute('SELECT ins.nombre, pf.direccion, pf.nombre, pf.hora_de_ingreso, pf.hora_de_salida, pf.numero_de_chaleco, pf.novedad FROM "A3_corredor" AS co, "A3_institucion" AS ins , "A3_corredor_puntos" AS cp, "A3_puntosfijos" AS pf, "A3_tipodecorredor" AS tdp WHERE tdp.id=co.tipo_de_corredor_id and ins.id = co.institucion_id AND cp.corredor_id = co.id AND pf.id = cp.puntosfijos_id ' );
    c1 = cur.fetchall()

    if(desde!='' and hasta !=''):
        cur.execute('SELECT co.id, tdp.nombre, co.fecha_de_creacion, us.first_name, us.last_name, co.direccion, co.hora_de_ingreso, co.hora_de_salida FROM "A3_corredor" AS co INNER JOIN "auth_user" AS us ON us.id = co.encargado_id INNER JOIN "A3_tipodecorredor" AS tdp  ON tdp.id=co.tipo_de_corredor_id WHERE co.fecha_de_creacion = %s and co.fecha_de_creacion = %s', (desde, hasta))
        corredor = cur.fetchall()
    else:
        cur.execute('SELECT co.id, tdp.nombre, co.fecha_de_creacion, us.first_name, us.last_name, co.direccion, co.hora_de_ingreso, co.hora_de_salida FROM "A3_corredor" AS co INNER JOIN "auth_user" AS us ON us.id = co.encargado_id INNER JOIN "A3_tipodecorredor" AS tdp  ON tdp.id=co.tipo_de_corredor_id ')
        corredor = cur.fetchall()

    print(corredor)

    cur.execute('SELECT tdp.id, tdp.nombre FROM "A3_tipodecorredor" AS tdp ;')
    corlista = cur.fetchall()

    cur.execute('SELECT * FROM "A3_images" ;')
    imagenes = cur.fetchall()

    return render(request, 'general.html', {'form':form,'data':c1, 'now':now, 'corredor':corredor, 'imagenes':imagenes, 'listacorredor':corlista})