from django.http import HttpResponse

def saludo(request):

    return HttpResponse("<html><body><h1>hola alumnos esta es nuestra primera página con Django</h1></body></html>")

def despedida(request):
    return HttpResponse("Hasta luego alumnos de Django")
