import os
import django
from decimal import Decimal

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'producto.settings')
django.setup()

from productos.models import Producto


def cargar_productos():

    productos = [
        Producto(
            nombre="Notebook Lenovo ThinkPad T480 Usado",
            descripcion="Notebook empresarial usado, batería al 80%, teclado retroiluminado.",
            precio=Decimal("250000"),
            cantidad=3
        ),
        Producto(
            nombre="iPhone 11 64GB Reacondicionado",
            descripcion="Equipo reacondicionado, batería nueva y pantalla sin rayas visibles.",
            precio=Decimal("320000"),
            cantidad=2
        ),
        Producto(
            nombre="Silla Gamer FuryX Segunda Mano",
            descripcion="Silla gamer usada en buen estado, cojines originales incluidos.",
            precio=Decimal("85000"),
            cantidad=5
        ),
        Producto(
            nombre="Bicicleta Mountain Bike Trek 3900",
            descripcion="Bicicleta usada poco tiempo, frenos revisados y asiento cambiado.",
            precio=Decimal("180000"),
            cantidad=1
        ),
        Producto(
            nombre="Cafetera Nespresso Essenza Mini Usada",
            descripcion="Cafetera compacta compatible con cápsulas Nespresso, en excelente estado.",
            precio=Decimal("45000"),
            cantidad=4
        ),
        Producto(
            nombre="Monitor Samsung 24'' Curvo Usado",
            descripcion="Monitor curvo Full HD, sin píxeles muertos, incluye cable HDMI.",
            precio=Decimal("65000"),
            cantidad=3
        ),
        Producto(
            nombre="Set de Herramientas Bosch 40 piezas",
            descripcion="Set completo de herramientas, 40 piezas, poco uso, ideal para hogar.",
            precio=Decimal("30000"),
            cantidad=6
        ),
        Producto(
            nombre="Lámpara de Pie Vintage Madera",
            descripcion="Lámpara de pie estilo vintage, base de madera natural y pantalla nueva.",
            precio=Decimal("20000"),
            cantidad=2
        ),
        Producto(
            nombre="Impresora HP DeskJet 2700 Usada",
            descripcion="Impresora multifunción usada, incluye cartuchos instalados con tinta.",
            precio=Decimal("25000"),
            cantidad=3
        ),
        Producto(
            nombre="Moledora de Café Manual Retro",
            descripcion="Moledora manual estilo retro, ideal para café de grano medio.",
            precio=Decimal("15000"),
            cantidad=7
        ),
    ]

    Producto.objects.bulk_create(productos)
    print("10 productos usados cargados con éxito")
    print(f"Total de productos en la base de datos: {Producto.objects.count()}")


if __name__ == "__main__":
    cargar_productos()
