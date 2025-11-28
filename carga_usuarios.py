import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'producto.settings')
django.setup()

from productos.models import Cliente  


def cargar_clientes():

    clientes = [
        Cliente(
            nombre="Ana Torres",
            email="ana.torres@example.com",
            telefono="+56 9 1111 1111"
        ),
        Cliente(
            nombre="Carlos Pérez",
            email="carlos.perez@example.com",
            telefono="+56 9 2222 2222"
        ),
        Cliente(
            nombre="María González",
            email="maria.gonzalez@example.com",
            telefono="+56 9 3333 3333"
        ),
    ]

    Cliente.objects.bulk_create(clientes)

    print("3 clientes creados con éxito")
    print(f"Total de clientes en la base de datos: {Cliente.objects.count()}")


if __name__ == "__main__":
    cargar_clientes()
