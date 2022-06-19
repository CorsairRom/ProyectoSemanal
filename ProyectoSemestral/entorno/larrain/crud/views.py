from datetime import datetime
from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth import authenticate, login
from django.contrib import messages
from datetime import datetime

from crud.forms import Custom, PersonaForm
from crud.models import Persona
# Create your views here.
def index(request):
    
    
    return render(request, "crud/index.html")





def registrar(request):
    data = {
        "form": Custom
    }
    if request.method == 'POST':
        formulario = Custom(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            #redirigir al inicio
            user = authenticate(username= formulario.cleaned_data["username"], password = formulario.cleaned_data["password1"])
            login(request, user)
            messages.success(request, "Te has registrado correctamente")
            return redirect(to="persona")
        data["form"]= formulario   
        
    return render(request, "registration/registrar.html", data)
def persona(request):
    form = PersonaForm(request.POST or None)
    ctx = {
        "form" : form
    }
    if request.method == "POST":
        form2 = PersonaForm(data=request.POST)
        if form2.is_valid():
            datos = form2.cleaned_data
            persona = Persona()
            persona.usuario = request.user
            persona.nombre = datos.get("nombre")
            persona.apellido = datos.get("apellido")
            persona.rut = datos.get("rut")
            persona.direccion = datos.get("direccion")
            persona.n_celular = datos.get("n_celular")
            persona.fecha_nacimiento = datos.get("fecha_nacimiento")
            persona.save()
            return redirect(index)
        else:
            return render(request, "registration/persona.html", {"form": form2})
   
    
    return render(request, "registration/persona.html", ctx)

