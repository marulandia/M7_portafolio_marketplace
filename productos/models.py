from django.db import models
from django.core.validators import MinValueValidator


class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True, null=True) 
    precio = models.DecimalField(
        max_digits=10, 
        decimal_places=2,
        validators=[MinValueValidator(0.01)],
        help_text="Precio debe ser mayor a 0.00"
    )
    cantidad = models.IntegerField(
        validators=[MinValueValidator(0)],
        help_text="Cantidad no puede ser negativa"
    )

    class Meta:
        ordering = ['nombre']
        indexes = [
            models.Index(fields=['nombre']),
        ]

    def __str__(self):
        return f"{self.nombre} - ${self.precio}"


class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    telefono = models.CharField(max_length=20)

    def __str__(self):
        return self.nombre


class PerfilCliente(models.Model):
    cliente = models.OneToOneField(Cliente, on_delete=models.CASCADE, related_name='perfil')
    direccion = models.CharField(max_length=200, blank=True, null=True)
    rut = models.CharField(max_length=20, blank=True, null=True)

    def __str__(self):
        return f"Perfil de {self.cliente.nombre}"


class Pedido(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name='pedidos')
    productos = models.ManyToManyField(Producto, related_name='pedidos')

    numero_pedido = models.CharField(max_length=20)
    fecha = models.DateField()
    total = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Pedido {self.numero_pedido} de {self.cliente.nombre}"
