import datetime
import os

from django.conf import settings
from django.http import HttpResponse
from django.template import Context
from django.template.loader import get_template

from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from xhtml2pdf import pisa
from cStringIO import StringIO
from centro.models import Alumnos,Cursos
from convivencia.models import Amonestaciones,Sanciones
from centro.views import ContarFaltas

from datetime import datetime


# Create your views here.


@login_required(login_url='/')
def imprimir_partes(request,curso):
	lista_alumnos = Alumnos.objects.filter(Unidad__id=curso)
	lista=zip(range(1,len(lista_alumnos)+1),lista_alumnos,ContarFaltas(lista_alumnos.values("id")))
	data={'alumnos':lista,'curso':Cursos.objects.get(id=curso)}
	# Render html content through html template with context
	return imprimir("pdf_partes.html",data,"partes.pdf")


@login_required(login_url='/')
def imprimir_show(request,tipo,mes,ano,dia):
	fecha=datetime(int(ano),int(mes),int(dia))
	if tipo=="amonestacion":
		datos=Amonestaciones.objects.filter(Fecha=fecha)
		titulo="Resumen de amonestaciones"
	if tipo=="sancion":
		datos=Sanciones.objects.filter(Fecha=fecha)
		titulo="Resumen de sanciones"
	
	datos=zip(range(1,len(datos)+1),datos,ContarFaltas(datos.values("IdAlumno")))
	data={'datos':datos,'tipo':tipo,'fecha':fecha,'titulo':titulo,tipo:True}
	return imprimir("pdf_resumen.html",data,"resumen_"+tipo+".pdf")	

@login_required(login_url='/')
def carta_amonestacion(request,mes,ano,dia):
	info={}
	contenido=""
	fecha2=datetime(int(ano),int(mes),int(dia))
	info["fecha"]="%s/%s/%s"%(dia,mes,ano)
	info["amonestaciones"]=Amonestaciones.objects.filter(Fecha=fecha2)

	for i in info["amonestaciones"]:
		info2={}
		info2["amonestacion"]=i
		info2["num_amon"]=str(len(Amonestaciones.objects.filter(IdAlumno_id=i.IdAlumno_id)))
		template = get_template("pdf_contenido_carta_amonestacion.html")
		contenido=contenido+ template.render(Context(info2))
		if i.id!=info["amonestaciones"].last().id:
			contenido=contenido+"<pdf:nextpage>"
	info["contenido"]=contenido
	return imprimir("pdf_carta.html",info,"carta_amonestacion"+".pdf")	
	


@login_required(login_url='/')
def carta_sancion(request,identificador):
	info2={}
	contenido=""
	
	info2["sancion"]=Sanciones.objects.get(id=identificador)
	info={}
	template = get_template("pdf_contenido_carta_sancion.html")
	info["contenido"]=template.render(Context(info2))	
	return imprimir("pdf_carta.html",info,"carta_sancion"+".pdf")	


	
def imprimir(temp,data,tittle):
	template = get_template(temp)
	pdf_data = template.render(Context(data))
	# Write PDF to file
	
	pdf = StringIO()
	pisa.CreatePDF(StringIO(pdf_data.encode('utf-8')), pdf)
	pdf.reset()
	response = HttpResponse(pdf.read(),content_type='application/pdf')
	response['Content-Disposition'] = 'attachment; filename="'+tittle+'"'
	return response