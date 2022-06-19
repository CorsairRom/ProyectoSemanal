from django.contrib import admin

from crud.models import Categoria, Persona, Producto

# Register your models here.

class ProductoAdmin(admin.ModelAdmin):
    list_display = ["nombre", "precio", "categoria", "stock"]
    list_editable = ["precio", "stock"]
    search_fields = ["nombre"]
    list_filter = ["categoria", "stock"]
    list_per_page = 10
    

    
admin.site.register(Categoria)
admin.site.register(Producto, ProductoAdmin)
admin.site.register(Persona)

