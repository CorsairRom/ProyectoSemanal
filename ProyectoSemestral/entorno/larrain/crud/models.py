from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Categoria(models.Model):
    nombre = models.CharField(max_length=50)
    
    def __str__(self):
        return self.nombre
    
class Producto(models.Model):
    nombre = models.CharField(max_length=50)
    precio = models.IntegerField()
    descripcion = models.TextField()
    stock = models.IntegerField()
    categoria = models.ForeignKey(Categoria, on_delete=models.PROTECT)
    imagen = models.ImageField(upload_to="producto", null=True)
    usuario = models.ForeignKey(User, blank= True, null= True, on_delete=models.CASCADE) #nuevo
    oferta = models.BooleanField(default=False)
    def __str__(self):
        return self.nombre

class Persona(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank= True)
    nombre = models.CharField( max_length=50)
    apellido = models.CharField( max_length=50)
    rut = models.CharField(unique=True, max_length=10)
    direccion = models.CharField( max_length=50)
    n_celular = models.CharField(max_length=10, verbose_name="Numero celular")
    fecha_nacimiento = models.DateField(null=True, blank=True)
    
    vendedor = models.BooleanField(default=False)
    
    def __str__(self):
        return self.nombre + ' ' + self.apellido