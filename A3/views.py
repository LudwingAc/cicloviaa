import datetime

import psycopg2
from django.shortcuts import render
import sqlite3

# Create your views here.
from A3.form import dateForm

def operativo(request, num, pag):

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

    cur.execute('SELECT ins.nombre, pf.direccion, pf.nombre, pf.numero_de_contrato, pf.novedad, pf.asistio, pf.inasistio, pf.retardo, pf.devolucion FROM "A3_corredor" AS co, "A3_institucion" AS ins , "A3_corredor_guardianes" AS cp, "A3_guardianes" AS pf, "A3_tipodecorredor" AS tdp WHERE tdp.id=co.tipo_de_corredor_id and ins.id = co.institucion_id AND cp.corredor_id = co.id AND pf.id = cp.guardianes_id ');
    c1 = cur.fetchall()

    # if(desde!='' and hasta !=''):
    #     cur.execute('SELECT co.id, tdp.nombre, co.fecha_de_creacion, us.first_name, us.last_name, co.direccion, co.hora_de_ingreso, co.hora_de_salida FROM "A3_corredor" AS co INNER JOIN "auth_user" AS us ON us.id = co.encargado_id INNER JOIN "A3_tipodecorredor" AS tdp  ON tdp.id=co.tipo_de_corredor_id WHERE co.id= %s and co.id=%s and co.fecha_de_creacion = %s and co.fecha_de_creacion = %s', (num, num, desde, hasta))
    #     corredor = cur.fetchall()
    # else:
    cur.execute('SELECT co.id, tdp.nombre, co.fecha_de_creacion, us.first_name, us.last_name, co.direccion, co.hora_de_ingreso, co.hora_de_salida, tdp.id FROM "A3_corredor" AS co INNER JOIN "auth_user" AS us ON us.id = co.encargado_id INNER JOIN "A3_tipodecorredor" AS tdp  ON tdp.id=co.tipo_de_corredor_id WHERE co.id=%s and co.id=%s',(pag,pag))
    corredor = cur.fetchall()


    cur.execute('SELECT co.id, tdp.nombre, co.fecha_de_creacion, us.first_name, us.last_name, co.direccion, co.hora_de_ingreso, co.hora_de_salida, co.tipo_de_corredor_id FROM "A3_corredor" AS co INNER JOIN "auth_user" AS us ON us.id = co.encargado_id INNER JOIN "A3_tipodecorredor" AS tdp  ON tdp.id=co.tipo_de_corredor_id WHERE co.tipo_de_corredor_id=%s and co.tipo_de_corredor_id=%s ',(num, num))
    filtro = cur.fetchall()

    cur.execute('SELECT tdp.id, tdp.nombre, tdp.fecha_de_creacion FROM "A3_tipodecorredor" AS tdp ;')
    corlista = cur.fetchall()

    cur.execute('SELECT * FROM "A3_images" ;')
    imagenes = cur.fetchall()

    cur.execute('SELECT co.desarrollo_de_la_jornada FROM "A3_corredor" AS co INNER JOIN "auth_user" AS us ON us.id = co.encargado_id INNER JOIN "A3_tipodecorredor" AS tdp  ON tdp.id=co.tipo_de_corredor_id WHERE co.id=%s and co.id=%s',(pag,pag))
    desarrollo = cur.fetchall()

    cur.execute('SELECT er.* FROM public."A3_corredor" AS co, "A3_corredor_eventos_realizados" AS ce, "A3_eventosrealizados" AS er WHERE co.id=%s and ce.corredor_id = %s',(pag,pag))
    eventos = cur.fetchall()

    cur.execute('SELECT ac.* FROM public."A3_corredor" AS co, "A3_corredor_activaciones" AS ap, "A3_activacionesyproyectosrealizados" AS ac WHERE co.id=%s and ap.corredor_id =%s',(pag,pag))
    activaciones = cur.fetchall()

    cur.execute('SELECT uda.* FROM "A3_corredor" AS co INNER JOIN "A3_corredor_unidades_de_apoyo" AS cua ON cua.corredor_id = co.id INNER JOIN "A3_unidadesdeapoyo" AS uda  ON cua.unidadesdeapoyo_id=uda.id WHERE co.id=%s and co.id=%s',(pag,pag))
    apoyo = cur.fetchall()

    cur.execute('SELECT co.solicitudes FROM "A3_corredor" AS co WHERE co.id=%s and co.id=%s',(pag,pag))
    solicitudes = cur.fetchall()

    cur.execute('SELECT ao.*, eps.nombre FROM "A3_corredor" AS co  INNER JOIN "A3_corredor_accidentes_ocurridos" AS cao ON cao.corredor_id = co.id INNER JOIN "A3_accidentesocurridos" AS ao  ON cao.accidentesocurridos_id=ao.id INNER JOIN "A3_eps" AS eps ON ao.eps_atendido_id = eps.id WHERE co.id=%s and co.id=%s', (pag, pag))
    accidente = cur.fetchall()

    cur.execute('SELECT usoi.* FROM "A3_corredor" AS co INNER JOIN "A3_corredor_unidades_solicitada_otras_inst" AS cusoi ON cusoi.corredor_id = co.id INNER JOIN "A3_unidadessolicitadasotrasinst" AS usoi  ON cusoi.unidadessolicitadasotrasinst_id=usoi.id WHERE co.id=%s and co.id=%s', (pag, pag))
    otras = cur.fetchall()

    return render(request, 'operativo.html', {'otras':otras,'accidente':accidente,'solicitudes':solicitudes,'apoyo':apoyo,'activaciones':activaciones,'eventos':eventos,'desarrollo':desarrollo,'pagina':num,'form':form,'data':c1, 'now':now, 'corredor':corredor, 'imagenes':imagenes, 'listacorredor':corlista, 'filtro':filtro})

def addpf(request, num, pag):

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

    cur.execute('SELECT uda.* FROM "A3_corredor" AS co INNER JOIN "A3_corredor_unidades_de_apoyo" as cuda ON cuda.corredor_id = co.id INNER JOIN "A3_unidadesdeapoyo" AS uda ON uda.id = cuda.unidadesdeapoyo_id WHERE co.id=%s and co.id=%s',(pag,pag));
    c1 = cur.fetchall()
    print(c1)

    # if(desde!='' and hasta !=''):
    #     cur.execute('SELECT co.id, tdp.nombre, co.fecha_de_creacion, us.first_name, us.last_name, co.direccion, co.hora_de_ingreso, co.hora_de_salida FROM "A3_corredor" AS co INNER JOIN "auth_user" AS us ON us.id = co.encargado_id INNER JOIN "A3_tipodecorredor" AS tdp  ON tdp.id=co.tipo_de_corredor_id WHERE co.id= %s and co.id=%s and co.fecha_de_creacion = %s and co.fecha_de_creacion = %s', (num, num, desde, hasta))
    #     corredor = cur.fetchall()
    # else:
    cur.execute('SELECT co.id, tdp.nombre, co.fecha_de_creacion, us.first_name, us.last_name, co.direccion, co.hora_de_ingreso, co.hora_de_salida, tdp.id FROM "A3_corredor" AS co INNER JOIN "auth_user" AS us ON us.id = co.encargado_id INNER JOIN "A3_tipodecorredor" AS tdp  ON tdp.id=co.tipo_de_corredor_id WHERE co.id=%s and co.id=%s',(pag,pag))
    corredor = cur.fetchall()


    cur.execute('SELECT co.id, tdp.nombre, co.fecha_de_creacion, us.first_name, us.last_name, co.direccion, co.hora_de_ingreso, co.hora_de_salida, co.tipo_de_corredor_id FROM "A3_corredor" AS co INNER JOIN "auth_user" AS us ON us.id = co.encargado_id INNER JOIN "A3_tipodecorredor" AS tdp  ON tdp.id=co.tipo_de_corredor_id WHERE co.tipo_de_corredor_id=%s and co.tipo_de_corredor_id=%s ',(num, num))
    filtro = cur.fetchall()

    cur.execute('SELECT tdp.id, tdp.nombre, tdp.fecha_de_creacion FROM "A3_tipodecorredor" AS tdp ;')
    corlista = cur.fetchall()

    cur.execute('SELECT * FROM "A3_images" ;')
    imagenes = cur.fetchall()


    return render(request, 'addPuntosFijos.html', {'pagina':num,'form':form,'data':c1, 'now':now, 'corredor':corredor, 'imagenes':imagenes, 'listacorredor':corlista, 'filtro':filtro})

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

    cur.execute('SELECT ins.nombre, pf.direccion, pf.nombre, pf.numero_de_contrato, pf.novedad, pf.asistio, pf.inasistio, pf.retardo, pf.devolucion FROM "A3_corredor" AS co, "A3_institucion" AS ins , "A3_corredor_guardianes" AS cp, "A3_guardianes" AS pf, "A3_tipodecorredor" AS tdp WHERE tdp.id=co.tipo_de_corredor_id and ins.id = co.institucion_id AND cp.corredor_id = co.id AND pf.id = cp.guardianes_id ' );
    c1 = cur.fetchall()
    print(c1)

    if(desde!='' and hasta !=''):
        cur.execute('SELECT co.id, tdp.nombre, co.fecha_de_creacion, us.first_name, us.last_name, co.direccion, co.hora_de_ingreso, co.hora_de_salida FROM "A3_corredor" AS co INNER JOIN "auth_user" AS us ON us.id = co.encargado_id INNER JOIN "A3_tipodecorredor" AS tdp  ON tdp.id=co.tipo_de_corredor_id WHERE co.fecha_de_creacion = %s and co.fecha_de_creacion = %s', (desde, hasta))
        corredor = cur.fetchall()
    else:
        cur.execute('SELECT co.id, tdp.nombre, co.fecha_de_creacion, us.first_name, us.last_name, co.direccion, co.hora_de_ingreso, co.hora_de_salida FROM "A3_corredor" AS co INNER JOIN "auth_user" AS us ON us.id = co.encargado_id INNER JOIN "A3_tipodecorredor" AS tdp  ON tdp.id=co.tipo_de_corredor_id ')
        corredor = cur.fetchall()

    cur.execute('SELECT tdp.id, tdp.nombre FROM "A3_tipodecorredor" AS tdp ;')
    corlista = cur.fetchall()

    cur.execute('SELECT * FROM "A3_images" ;')
    imagenes = cur.fetchall()

    return render(request, 'general.html', {'form':form,'data':c1, 'now':now, 'corredor':corredor, 'imagenes':imagenes, 'listacorredor':corlista})