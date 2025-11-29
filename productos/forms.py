from django import forms
from django.core.exceptions import ValidationError
from .models import Producto, Cliente, PerfilCliente, Pedido


class BaseForm(forms.ModelForm):
    """Clase base para aplicar Bootstrap a todos los formularios"""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs.update({
                'class': 'form-control',
                'placeholder': f'Ingrese {field.label.lower()}',
            })


class ProductoForm(BaseForm):
    class Meta:
        model = Producto
        fields = ['nombre', 'descripcion', 'precio', 'cantidad']
        widgets = {
            'nombre': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Nombre del producto',
                'required': True,
            }),
            'descripcion': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Descripción (opcional)',
                'rows': 3,
            }),
            'precio': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ej: 99.99',
                'step': '0.01',
                'min': '0.01',
            }),
            'cantidad': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Stock disponible',
                'min': '0',
            }),
        }

    def clean_precio(self):
        precio = self.cleaned_data.get('precio')
        if precio and precio <= 0:
            raise ValidationError('El precio debe ser mayor a 0.00')
        return precio

    def clean_cantidad(self):
        cantidad = self.cleaned_data.get('cantidad')
        if cantidad and cantidad < 0:
            raise ValidationError('La cantidad no puede ser negativa')
        return cantidad


class ClienteForm(BaseForm):
    class Meta:
        model = Cliente
        fields = ['nombre', 'email', 'telefono']
        widgets = {
            'nombre': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Nombre completo',
                'required': True,
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'correo@ejemplo.com',
                'required': True,
            }),
            'telefono': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': '+56 9 1234 5678',
                'required': True,
            }),
        }

    def clean_email(self):
        email = self.cleaned_data.get('email')
        # Si es edición, excluir el cliente actual
        if email:
            qs = Cliente.objects.filter(email=email)
            if self.instance.pk:
                qs = qs.exclude(pk=self.instance.pk)
            if qs.exists():
                raise ValidationError('Este email ya está registrado')
        return email


class PerfilClienteForm(BaseForm):
    class Meta:
        model = PerfilCliente
        fields = ['direccion', 'rut']
        widgets = {
            'direccion': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Calle, número, ciudad',
            }),
            'rut': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'XX.XXX.XXX-K',
            }),
        }


class PedidoForm(BaseForm):
    class Meta:
        model = Pedido
        fields = ['cliente', 'productos', 'numero_pedido', 'fecha', 'total']
        widgets = {
            'cliente': forms.Select(attrs={
                'class': 'form-select',
                'required': True,
            }),
            'productos': forms.CheckboxSelectMultiple(attrs={
                'class': 'form-check-input',
            }),
            'numero_pedido': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ej: PED-001',
                'required': True,
            }),
            'fecha': forms.DateInput(attrs={
                'class': 'form-control',
                'type': 'date',
                'required': True,
            }),
            'total': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Total del pedido',
                'step': '0.01',
                'min': '0.01',
            }),
        }

    def clean(self):
        cleaned_data = super().clean()
        productos = cleaned_data.get('productos')
        total = cleaned_data.get('total')

        if not productos:
            raise ValidationError('Debe seleccionar al menos un producto')

        if total and total <= 0:
            raise ValidationError('El total debe ser mayor a 0')

        return cleaned_data
