from django.http.response import HttpResponse
from django.shortcuts import render

# Create your views here.

#Primer vista
def inicio(request):

    #return HttpResponse("Esto es una prueba del inicio")
    return render(request, 'AppCoder/inicio.html')

def jugadores(request):

    return render (request, 'AppCoder/jugadores.html')