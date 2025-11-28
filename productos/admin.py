from django.contrib import admin
from .models import Producto, Cliente, PerfilCliente, Pedido


@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'precio', 'cantidad')  
    search_fields = ('nombre', 'descripcion')          
    list_filter = ('cantidad',)                        
    ordering = ('nombre',)                             



@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'email', 'telefono')
    search_fields = ('nombre', 'email')
    ordering = ('nombre',)



@admin.register(PerfilCliente)
class PerfilClienteAdmin(admin.ModelAdmin):
    list_display = ('cliente', 'direccion', 'rut')
    search_fields = ('cliente__nombre', 'rut')
    ordering = ('cliente',)



@admin.register(Pedido)
class PedidoAdmin(admin.ModelAdmin):
    list_display = ('numero_pedido', 'cliente', 'fecha', 'total')
    search_fields = ('numero_pedido', 'cliente__nombre')
    list_filter = ('fecha',)
    ordering = ('-fecha',)
    filter_horizontal = ('productos',)  
