from django.http import HttpResponse
import datetime
from django.template import Template, Context

def saludo(request):
    doc_externo=open("C:/Users/jlcal/Desktop/ProyectosDjango/Proyecto1/Proyecto1/plantillas/miplantilla.html")
    plt=Template(doc_externo.read())
    doc_externo.close()
    ctx=Context()
    documento=plt.render(ctx)
    return HttpResponse(documento)

def despedida(request):
    return HttpResponse("Hasta luego alumnos de Django")

def dameFecha(request):
    fecha_actual=datetime.datetime.now()
    documento2="""<html> 
    <body>
    <h2>
    Fecha y hora actuales {}
    </h2>
    </body>
    </html>""".format(fecha_actual)
    return HttpResponse(documento2)

#paso de parametros
def calculaEdad(request,edad, agno):
    periodo=agno-2024
    edadFutura=edad+periodo
    documento=f"<html><body><h2> En el año {agno} tendrás {edadFutura} años</h2></body></html> "
    return HttpResponse(documento)

