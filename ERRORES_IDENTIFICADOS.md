# 🐛 Documento de Errores Identificados

**Proyecto**: Marketplace de Productos  
**Fecha**: Noviembre 28, 2025  
**Estado**: Errores Críticos Detectados

---

## 📊 Tabla de Errores por Prioridad

| # | Área | Problema | Prioridad | Estado |
|---|------|----------|-----------|--------|
| 1 | Seguridad | Credenciales MySQL hardcodeadas en settings.py | 🔴 ALTA | ❌ Sin corregir |
| 2 | Templates | Referencias a campos inexistentes (categoria, etiquetas) | 🔴 ALTA | ❌ Sin corregir |
| 3 | Validación | Cantidad y precio pueden ser negativos | 🟡 MEDIA | ❌ Sin corregir |
| 4 | Autenticación | Login URL configurada incorrectamente en settings.py | 🔴 ALTA | ❌ Sin corregir |

---

## 🔴 ERRORES CON PRIORIDAD ALTA

### Error #1: Credenciales MySQL Hardcodeadas

**Archivo**: `producto/settings.py`  
**Línea**: 83-91  
**Severidad**: 🔴 CRÍTICA  
**Impacto**: Riesgo de seguridad en producción

#### Problema Actual:
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'market_producto',
        'USER': 'root',
        'PASSWORD': '1234',  # ⚠️ CONTRASEÑA EXPUESTA
        'HOST': '127.0.0.1',
        'PORT': '3306',
    }
}
```

#### Por Qué es Peligroso:
- ✋ Las credenciales están visibles en el código fuente
- ✋ Si el repositorio se vuelve público, cualquiera puede acceder a la BD
- ✋ Incumple estándares de seguridad OWASP
- ✋ No cumple GDPR ni regulaciones de seguridad

#### Solución Recomendada:
**Usar variables de entorno con `python-decouple`**

1. **Instalar la dependencia**:
```bash
pip install python-decouple
```

2. **Crear archivo `.env` en la raíz del proyecto**:
```
# .env
DB_ENGINE=django.db.backends.mysql
DB_NAME=market_producto
DB_USER=root
DB_PASSWORD=1234
DB_HOST=127.0.0.1
DB_PORT=3306
SECRET_KEY=django-insecure-h5%cq#b!%8u4dlo@%x0t=up4bn!i@p%esy1(op#a@0z#(k^3*!
DEBUG=True
```

3. **Actualizar `settings.py`**:
```python
from decouple import config

# Database
DATABASES = {
    'default': {
        'ENGINE': config('DB_ENGINE'),
        'NAME': config('DB_NAME'),
        'USER': config('DB_USER'),
        'PASSWORD': config('DB_PASSWORD'),
        'HOST': config('DB_HOST'),
        'PORT': config('DB_PORT'),
    }
}

SECRET_KEY = config('SECRET_KEY')
DEBUG = config('DEBUG', default=False, cast=bool)
```

4. **Agregar `.env` a `.gitignore`**:
```
.env
*.pyc
__pycache__/
venv/
```

---

### Error #2: Referencias a Campos Inexistentes en Templates

**Archivo**: `productos/templates/productos/lista_productos.html`  
**Línea**: 13-19  
**Severidad**: 🔴 CRÍTICA  
**Impacto**: Mostrar errores en la página o campos vacíos

#### Problema Actual:
```html
<table class="table table-striped">
    <thead>
        <tr>
            <th>Nombre</th>
            <th>Categoría</th>          <!-- ⚠️ Campo inexistente -->
            <th>Precio</th>
            <th>Etiquetas</th>          <!-- ⚠️ Campo inexistente -->
            <th>Acciones</th>
        </tr>
    </thead>
    <tbody>
        {% for p in productos %}
        <tr>
            <td>{{ p.nombre }}</td>
            <td>{{ p.categoria.nombre }}</td>  <!-- ⚠️ AttributeError -->
            <td>${{ p.precio }}</td>
            <td>
                {% for et in p.etiquetas.all %}  <!-- ⚠️ AttributeError -->
                    <span class="badge bg-secondary">{{ et.nombre }}</span>
                {% empty %}
                    <span class="text-muted">Sin etiquetas</span>
                {% endfor %}
            </td>
```

#### Por Qué es un Error:
- ✋ El modelo `Producto` NO tiene campo `categoria`
- ✋ El modelo `Producto` NO tiene campo `etiquetas`
- ✋ Django lanzará error `AttributeError` al renderizar el template
- ✋ Los usuarios verán una página rota o blanca

#### Verificación del Modelo:
En `productos/models.py`, el modelo Producto actual es:
```python
class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True, null=True) 
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    cantidad = models.IntegerField()
    # ⚠️ NO HAY: categoria, etiquetas
```

#### Soluciones Posibles:

**Opción A: Eliminar referencias (Rápida)**
```html
<table class="table table-striped">
    <thead>
        <tr>
            <th>Nombre</th>
            <th>Descripción</th>
            <th>Precio</th>
            <th>Cantidad</th>
            <th>Acciones</th>
        </tr>
    </thead>
    <tbody>
        {% for p in productos %}
        <tr>
            <td>{{ p.nombre }}</td>
            <td>{{ p.descripcion|truncatewords:10 }}</td>
            <td>${{ p.precio }}</td>
            <td>{{ p.cantidad }}</td>
            <td>
                <a href="{% url 'detalle_producto' p.pk %}" class="btn btn-sm btn-info">Ver</a>
                <a href="{% url 'editar_producto' p.pk %}" class="btn btn-sm btn-warning">Editar</a>
                <a href="{% url 'eliminar_producto' p.pk %}" class="btn btn-sm btn-danger">Eliminar</a>
            </td>
        </tr>
        {% endfor %}
    </tbody>
</table>
```

**Opción B: Crear los modelos faltantes (Mejor a largo plazo)**

Crear modelos Categoria y Etiqueta:
```python
class Categoria(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True, null=True)
    
    def __str__(self):
        return self.nombre


class Etiqueta(models.Model):
    nombre = models.CharField(max_length=50)
    
    def __str__(self):
        return self.nombre


class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True, null=True) 
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    cantidad = models.IntegerField()
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, null=True, blank=True)
    etiquetas = models.ManyToManyField(Etiqueta, blank=True)
    
    def __str__(self):
        return self.nombre
```

Luego ejecutar:
```bash
python manage.py makemigrations
python manage.py migrate
```

---

### Error #3: Login URL Configurada Incorrectamente

**Archivo**: `producto/settings.py`  
**Línea**: 129  
**Severidad**: 🔴 CRÍTICA  
**Impacto**: Redirección a URL inexistente después del login

#### Problema Actual:
```python
# En settings.py
LOGIN_URL = '/accounts/login/'
LOGIN_REDIRECT_URL = '/'
```

#### Por Qué es un Error:
- ✋ Se configura LOGIN_URL como `/accounts/login/`
- ✋ Pero en `productos/urls.py` NO existe esta ruta
- ✋ Las vistas usan `{% url 'login' %}` (nombre de ruta)
- ✋ Si Django intenta redirigir con LOGIN_URL, llegará a 404

#### Verificación de URLs:
En `productos/urls.py` solo existen:
```python
path('', views.index, name='index'),
path('productos/', views.lista_productos, name='lista_productos'),
path('pedidos/', views.lista_pedidos, name='lista_pedidos'),
# ... otras rutas
# ⚠️ NO HAY RUTA DE LOGIN
```

#### Solución:

**Opción A: Usar nombre de ruta en settings.py**
```python
# En settings.py
LOGIN_URL = 'login'  # Usar el nombre de la ruta
LOGIN_REDIRECT_URL = '/'
```

**Opción B: Crear la ruta de login explícitamente**

1. En `producto/urls.py`:
```python
from django.urls import path, include
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', include('productos.urls')),
    path('accounts/login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('accounts/logout/', auth_views.LogoutView.as_view(), name='logout'),
]
```

2. Luego en settings.py:
```python
LOGIN_URL = '/accounts/login/'
LOGIN_REDIRECT_URL = '/'
```

---

## 🟡 ERRORES CON PRIORIDAD MEDIA

### Error #4: Validación - Cantidad y Precio Pueden Ser Negativos

**Archivo**: `productos/models.py`  
**Línea**: 3-9  
**Severidad**: 🟡 MEDIA  
**Impacto**: Datos inválidos en base de datos

#### Problema Actual:
```python
class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True, null=True) 
    precio = models.DecimalField(max_digits=10, decimal_places=2)  # ⚠️ Sin validación
    cantidad = models.IntegerField()  # ⚠️ Sin validación
```

#### Ejemplos de Valores Inválidos Posibles:
- Producto con precio = -100
- Producto con cantidad = -50
- Producto con precio = 0
- Producto con cantidad = 0

#### Por Qué es un Error:
- ✋ No tiene sentido un producto con precio negativo
- ✋ No tiene sentido un producto con cantidad negativa
- ✋ Crea inconsistencias en el sistema
- ✋ Puede causar errores en cálculos (especialmente en pedidos)

#### Solución:

Agregar validadores en el modelo:

```python
from django.core.validators import MinValueValidator, DecimalValidator

class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True, null=True) 
    precio = models.DecimalField(
        max_digits=10, 
        decimal_places=2,
        validators=[MinValueValidator(0.01)]  # Mínimo 0.01
    )
    cantidad = models.IntegerField(
        validators=[MinValueValidator(0)]  # Mínimo 0
    )

    def __str__(self):
        return self.nombre
```

También agregar validación en el formulario:

```python
# En productos/forms.py
from django import forms
from .models import Producto

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['nombre', 'descripcion', 'precio', 'cantidad']
        
    def clean(self):
        cleaned_data = super().clean()
        precio = cleaned_data.get('precio')
        cantidad = cleaned_data.get('cantidad')
        
        if precio and precio <= 0:
            raise forms.ValidationError('El precio debe ser mayor a 0')
        
        if cantidad and cantidad < 0:
            raise forms.ValidationError('La cantidad no puede ser negativa')
        
        return cleaned_data
```

Luego ejecutar migraciones:
```bash
python manage.py makemigrations
python manage.py migrate
```

---

## 📋 Tabla de Soluciones Recomendadas

| Error | Solución | Tiempo Est. | Complejidad |
|-------|----------|------------|-------------|
| Credenciales hardcodeadas | Usar .env con python-decouple | 15 min | Baja |
| Referencias a campos inexistentes | Opción A: eliminar / Opción B: crear modelos | 20 min / 45 min | Baja / Media |
| Login URL incorrecta | Definir ruta o usar nombre | 10 min | Baja |
| Validación faltante | Agregar validators | 20 min | Baja |

---

## ✅ Orden Recomendado para Corregir

### Paso 1: Seguridad (INMEDIATO)
```bash
1. pip install python-decouple
2. Crear archivo .env
3. Actualizar settings.py
4. Agregar .gitignore
```

### Paso 2: Templates (INMEDIATO)
```bash
1. Corregir lista_productos.html (Opción A rápida)
2. O crear modelos Categoria y Etiqueta (Opción B)
```

### Paso 3: Autenticación (EN ESTA SESIÓN)
```bash
1. Definir ruta de login en urls.py
2. Actualizar settings.py
```

### Paso 4: Validación (EN PRÓXIMA ITERACIÓN)
```bash
1. Agregar validadores en models.py
2. Agregar validación en forms.py
3. Ejecutar migraciones
4. Hacer tests
```

---

## 🔍 Checklist de Verificación

### Para Seguridad:
- [ ] Instalar python-decouple
- [ ] Crear .env con credenciales
- [ ] Actualizar settings.py
- [ ] Agregar .env a .gitignore
- [ ] Verificar que settings.py no expone credenciales
- [ ] Cambiar SECRET_KEY en producción
- [ ] Cambiar DEBUG a False en producción

### Para Templates:
- [ ] Corregir referencias en lista_productos.html
- [ ] O crear modelos Categoria y Etiqueta
- [ ] Hacer migraciones si se crean modelos
- [ ] Probar que la página carga sin errores

### Para Autenticación:
- [ ] Definir ruta de login
- [ ] Actualizar LOGIN_URL en settings.py
- [ ] Probar que el login redirige correctamente

### Para Validación:
- [ ] Agregar validadores en Producto
- [ ] Agregar clean() en formulario
- [ ] Hacer migraciones
- [ ] Probar que rechaza valores negativos

---

## 📝 Resumen Ejecutivo

**Errores Críticos Encontrados**: 4  
**Prioridad Alta**: 3  
**Prioridad Media**: 1  

**Impacto General**: El proyecto funciona, pero tiene vulnerabilidades de seguridad y errores que pueden causar problemas en producción.

**Tiempo Total de Corrección**: ~80-100 minutos  
**Recomendación**: Corregir inmediatamente los errores de prioridad alta antes de desplegar.

