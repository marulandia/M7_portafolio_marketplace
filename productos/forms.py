from django import forms
from .models import Producto, Cliente, PerfilCliente, Pedido


class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['nombre', 'descripcion', 'precio', 'cantidad']


class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['nombre', 'email', 'telefono']


class PerfilClienteForm(forms.ModelForm):
    class Meta:
        model = PerfilCliente
        fields = ['direccion', 'rut']


class PedidoForm(forms.ModelForm):
    class Meta:
        model = Pedido
        fields = ['cliente', 'productos', 'numero_pedido', 'fecha', 'total']
        widgets = {
            'cliente': forms.Select(),
            'productos': forms.SelectMultiple(),
            'fecha': forms.DateInput(attrs={'type': 'date'}),
        }
