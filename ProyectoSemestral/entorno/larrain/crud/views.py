from datetime import datetime
from django.shortcuts import render
from datetime import datetime
# Create your views here.
def index(request):
    
    mensaje= "hola mundo"
    fecha = datetime.now()
    ctx={
        "msg": mensaje,
        "fecha": fecha,
    }
    return render(request, "crud/index.html", ctx)


def sesion(request):
    
    
    return render(request, "crud/sesion.html")


def registrar(request):
    
    
    return render(request, "crud/registrar.html")