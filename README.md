# Marketplace de productos de Maru y gatitas 

Sistema de gestión de productos, clientes y pedidos desarrollado con Django.

## 📋 Descripción 

Este es un marketplace Django que permite gestionar:
- **Productos**: Crear, editar, eliminar y listar productos con precios y cantidades
- **Clientes**: Gestionar información de clientes con perfiles detallados
- **Pedidos**: Crear y administrar pedidos asociados a clientes

## 🏗️ Estructura 

```
Productos/
├── producto/                 # Configuración principal de Django
│   ├── settings.py          # Configuración de la aplicación
│   ├── urls.py              # Rutas principales
│   ├── wsgi.py              # WSGI para producción
│   └── asgi.py              # ASGI para desarrollo
│
├── productos/               # Aplicación principal
│   ├── models.py            # Modelos de datos
│   ├── views.py             # Vistas (lógica del negocio)
│   ├── forms.py             # Formularios
│   ├── urls.py              # Rutas de la app
│   ├── admin.py             # Configuración del admin
│   ├── migrations/          # Migraciones de BD
│   └── templates/           # Plantillas HTML
│       ├── base.html
│       ├── index.html
│       ├── login.html
│       ├── productos/       # Templates de productos
│       ├── clientes/        # Templates de clientes
│       └── pedidos/         # Templates de pedidos
│
├── manage.py                # Utilidad de Django
├── carga_productos.py       # Script de carga inicial de datos
└── carga_usuarios.py        # Script de carga de usuarios
```

## 🗄️ Modelos de datos

### Producto
```python
- nombre: CharField(100)
- descripcion: TextField (opcional)
- precio: DecimalField (2 decimales)
- cantidad: IntegerField
```

### Cliente
```python
- nombre: CharField(100)
- email: EmailField (único)
- telefono: CharField(20)
```

### PerfilCliente
```python
- cliente: OneToOneField (relación 1:1 con Cliente)
- direccion: CharField(200, opcional)
- rut: CharField(20, opcional)
```

### Pedido
```python
- cliente: ForeignKey (relación con Cliente)
- productos: ManyToManyField (relación N:N con Producto)
- numero_pedido: CharField(20)
- fecha: DateField
- total: DecimalField (2 decimales)
```

## 🔐 Sistema de autenticación y permisos

El proyecto usa el sistema de autenticación de Django con control de permisos:

### Decoradores de vista
- `@login_required`: Requiere usuario autenticado
- `@permission_required()`: Requiere permisos específicos
- `@superuser_required`: Solo para superusuarios

### Permisos configurados
- `productos.add_producto`: Crear productos
- `productos.change_producto`: Editar productos
- `productos.delete_producto`: Eliminar productos
- `productos.add_cliente`: Crear clientes
- `productos.change_cliente`: Editar clientes
- `productos.delete_cliente`: Eliminar clientes
- `productos.add_pedido`: Crear pedidos
- `productos.change_pedido`: Editar pedidos
- `productos.delete_pedido`: Eliminar pedidos

## 🚀 Instalación y configuración

### Requisitos previos
- Python 3.8+
- pip (gestor de paquetes)

### Pasos de instalación

1. **Clonar el repositorio**
```bash
git clone https://github.com/marulandia/M7_portafolio_marketplace.git
cd Productos
```

2. **Crear entorno virtual**
```bash
python -m venv venv
# En Windows:
venv\Scripts\activate
# En Linux/Mac:
source venv/bin/activate
```

3. **Instalar dependencias**
```bash
pip install django
```

4. **Realizar migraciones**
```bash
python manage.py migrate
```

5. **Cargar datos iniciales**
```bash
# Cargar usuarios
python carga_usuarios.py

# Cargar productos
python carga_productos.py
```

6. **Crear superusuario**
```bash
python manage.py createsuperuser
```

7. **Ejecutar el servidor**
```bash
python manage.py runserver
```

El servidor estará disponible en: `http://127.0.0.1:8000/`

## 📄 Rutas principales

### Páginas públicas
- `/` - Página de inicio
- `/productos/` - Listado de productos
- `/productos/<id>/` - Detalle de producto
- `/login/` - Formulario de login

### Productos (autenticado)
- `/productos/crear/` - Crear producto
- `/productos/<id>/editar/` - Editar producto
- `/productos/<id>/eliminar/` - Eliminar producto

### Clientes (autenticado)
- `/clientes/` - Listado de clientes
- `/clientes/<id>/` - Detalle de cliente
- `/clientes/crear/` - Crear cliente
- `/clientes/<id>/editar/` - Editar cliente
- `/clientes/<id>/eliminar/` - Eliminar cliente

### Pedidos (autenticado)
- `/pedidos/` - Listado de pedidos
- `/pedidos/<id>/` - Detalle de pedido
- `/pedidos/crear/` - Crear pedido
- `/pedidos/<id>/editar/` - Editar pedido
- `/pedidos/<id>/eliminar/` - Eliminar pedido

## 🎨 Templates

El proyecto utiliza Bootstrap para el diseño responsivo. Los templates están organizados en:

- **base.html**: Template base con navegación y estructura común
- **login.html**: Formulario de autenticación
- **productos/**: Templates para gestión de productos
- **clientes/**: Templates para gestión de clientes
- **pedidos/**: Templates para gestión de pedidos

### Estructura común de templates
- `lista_*.html`: Listado con tabla
- `detalle_*.html`: Detalles del objeto
- `crear_*.html`: Formulario de creación
- `editar_*.html`: Formulario de edición
- `eliminar_*.html`: Confirmación de eliminación

## 🔧 Administración

Accede al panel de administración en: `http://127.0.0.1:8000/admin/`

- Usuario: (superuser creado)
- Contraseña: (la ingresada durante createsuperuser)

En el admin puedes:
- Gestionar usuarios y permisos
- Ver y editar productos, clientes y pedidos
- Gestionar perfiles de clientes

## 📦 Scripts de utilidad

### carga_usuarios.py
Carga usuarios iniciales en la base de datos con diferentes roles y permisos.

### carga_productos.py
Carga un catálogo inicial de productos de ejemplo.

## 🛠️ Tecnologías utilizadas

- **Django 5.2.8**: Framework web Python
- **Bootstrap**: Framework CSS responsive
- **SQLite**: Base de datos (por defecto)
- **Python 3**: Lenguaje de programación

## 📝 Funcionalidades principales

### Gestión de productos
- Listar todos los productos
- Ver detalles de cada producto
- Crear nuevos productos (requiere autenticación)
- Editar productos existentes
- Eliminar productos

### Gestión de clientes
- Listar clientes
- Ver perfil completo del cliente
- Crear nuevos clientes
- Editar información de cliente
- Eliminar clientes
- Gestionar perfiles adicionales

### Gestión de Pedidos
- Crear pedidos asociados a clientes
- Vincular múltiples productos a un pedido
- Editar pedidos existentes
- Eliminar pedidos
- Ver historial de pedidos por cliente

## 🔒 Seguridad

- Protección CSRF activada
- Autenticación de usuarios
- Sistema de permisos granular
- Validación de formularios
- Contraseñas hasheadas

## 📈 Próximas mejoras

- [ ] Sistema de carrito de compras
- [ ] Pasarela de pago
- [ ] Notificaciones por email
- [ ] Búsqueda avanzada de productos
- [ ] Filtros por categoría
- [ ] API REST

## 👨‍💻 Autor

**Marulandia** - [GitHub](https://github.com/marulandia)

## 📄 Licencia

Este proyecto está bajo licencia MIT.

## 📞 Soporte

Para reportar problemas o sugerencias, abre un issue en el repositorio.

---

**Última actualización**: Noviembre 2025
