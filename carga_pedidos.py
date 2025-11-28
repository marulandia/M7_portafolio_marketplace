import os
import django
from decimal import Decimal
from datetime import date

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'producto.settings')
django.setup()

from productos.models import Cliente, Producto, Pedido


def crear_pedido(numero, cliente, items, fecha):
    """
    items: lista de tuplas (producto, cantidad)
    """
    total = sum(p.precio * cantidad for p, cantidad in items)

    pedido = Pedido.objects.create(
        cliente=cliente,
        numero_pedido=numero,
        fecha=fecha,
        total=total,
    )

    # Asociamos solo los productos (la cantidad es "lógica" para el total)
    pedido.productos.set([p for p, _ in items])

    return pedido


def cargar_pedidos():
    # Ajusta estos correos si tus clientes tienen otros
    ana = Cliente.objects.get(email="ana.torres@example.com")
    carlos = Cliente.objects.get(email="carlos.perez@example.com")
    maria = Cliente.objects.get(email="maria.gonzalez@example.com")

    productos = list(Producto.objects.all())

    if len(productos) < 5:
        raise ValueError("Se necesitan al menos 5 productos cargados para este ejemplo.")

    p1, p2, p3, p4, p5 = productos[:5]

    # Pedido 1: Ana compra notebook + monitor
    crear_pedido(
        numero="P-0001",
        cliente=ana,
        items=[
            (p1, 1),  # ejemplo: Notebook
            (p4, 1),  # ejemplo: Bicicleta / Monitor, según tu catálogo
        ],
        fecha=date(2025, 11, 20),
    )

    # Pedido 2: Carlos compra iPhone
    crear_pedido(
        numero="P-0002",
        cliente=carlos,
        items=[
            (p2, 1),
        ],
        fecha=date(2025, 11, 21),
    )

    # Pedido 3: María compra silla gamer + lámpara
    crear_pedido(
        numero="P-0003",
        cliente=maria,
        items=[
            (p3, 1),
            (p5, 2),
        ],
        fecha=date(2025, 11, 22),
    )

    # Pedido 4: Ana compra cafetera + moledora
    crear_pedido(
        numero="P-0004",
        cliente=ana,
        items=[
            (p5, 1),
            (p3, 1),
        ],
        fecha=date(2025, 11, 23),
    )

    # Pedido 5: Carlos compra un mix de productos
    crear_pedido(
        numero="P-0005",
        cliente=carlos,
        items=[
            (p1, 1),
            (p2, 1),
            (p5, 1),
        ],
        fecha=date(2025, 11, 24),
    )

    print("5 pedidos creados con éxito")
    print(f"Total de pedidos en la base de datos: {Pedido.objects.count()}")


if __name__ == "__main__":
    cargar_pedidos()
