from crud.views import index, registrar, sesion

from django.urls import  path

urlpatterns = [
    path('', index, name="index"),
    path('sesion/', sesion, name="sesion"),
    path('registrar/', registrar, name="registrar"),
    
]