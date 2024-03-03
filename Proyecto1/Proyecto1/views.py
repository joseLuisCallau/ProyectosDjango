from django.http import HttpResponse
import datetime

def saludo(request):
    documento="""
    <html>
    <body>
    <h1>hola alumnos esta es nuestra primera página con Django</h1>
    </body>
    </html>
    """
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