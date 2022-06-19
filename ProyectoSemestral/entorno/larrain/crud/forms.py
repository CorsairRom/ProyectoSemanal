from django.contrib.auth.forms import UserCreationForm
from django import forms
from crud.models import Persona, Producto


class ProductoForm(forms.ModelForm):
    
    class Meta:
        model = Producto
        fields = ["nombre", "precio", "descripcion", "stock", "categoria", "imagen"]#nuevo
        exclude = ("usuario",)#nuevo

class Custom (UserCreationForm):
    pass

class PersonaForm(forms.ModelForm):
    fecha_nacimiento=forms.DateField(required=True,widget=forms.SelectDateWidget(attrs=({'style': 'width: 14%; display: inline;', 'class': 'mx-1'})))
    
    class Meta:
        model = Persona
        field = ["nombre", "apellido", "rut", "direccion", "n_celular", "fecha_nacimiento"]
        exclude = ("usuario", "vendedor",)