from crud.views import index, persona, registrar

from django.urls import  path

urlpatterns = [
    path('', index, name="index"),
    path('registrar/', registrar, name="registrar"),
    path('persona/', persona, name="persona"),
    
]