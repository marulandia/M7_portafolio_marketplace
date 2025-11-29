# 📋 Guía para Aplicar los Cambios

**Última Actualización**: Noviembre 29, 2025

---

## 🚀 Pasos a Seguir

### Paso 1: Actualizar Dependencias
```bash
pip install python-decouple
```

### Paso 2: Verificar Archivos Creados
Confirma que existan estos archivos en la raíz del proyecto:
- ✅ `.env` - Contiene variables de entorno
- ✅ `.gitignore` - Protege archivos sensibles

### Paso 3: Ejecutar Migraciones
Los validadores en los modelos requieren migración:
```bash
python manage.py makemigrations
python manage.py migrate
```

### Paso 4: Probar el Servidor
```bash
python manage.py runserver
```

Verifica que:
- ✅ El login funciona sin errores 404
- ✅ El logout redirige correctamente
- ✅ Las listas de productos, clientes y pedidos se cargan sin errores
- ✅ Los formularios rechazan valores negativos

### Paso 5: Pruebas Manuales

#### Test 1: Crear Producto con Precio Negativo
1. Ir a `/productos/crear/`
2. Intentar crear con precio = -100
3. Debe mostrar error: "El precio debe ser mayor a 0.00"

#### Test 2: Crear Producto con Cantidad Negativa
1. Ir a `/productos/crear/`
2. Intentar crear con cantidad = -5
3. Debe mostrar error: "La cantidad no puede ser negativa"

#### Test 3: Crear Cliente con Email Duplicado
1. Crear cliente con email: `test@example.com`
2. Intentar crear otro cliente con el mismo email
3. Debe mostrar error: "Este email ya está registrado"

#### Test 4: Login/Logout
1. Hacer logout
2. Debe redirigir a index
3. Hacer login
4. Debe redirigir a index

#### Test 5: Permisos en Botones
1. Como usuario no autenticado: Ver solo botón "Ver" en productos
2. Como usuario autenticado sin permisos: Ver solo botones permitidos
3. Como admin: Ver todos los botones

### Paso 6: Subir Cambios a Git
```bash
# Ver cambios
git status

# Agregar todos los cambios
git add .

# Crear commit descriptivo
git commit -m "refactor: Mejoras de seguridad, validación y UX

- Agregados validadores en modelo Producto (precio > 0, cantidad >= 0)
- Movidas credenciales a .env con python-decouple
- Refactorizado sistema de login (nombres de rutas en lugar de URLs)
- Mejorado diseño de templates (menos repetición, más responsive)
- Refactorizados formularios con validación y Bootstrap
- Limpiadas referencias a campos inexistentes en templates"

# Subir
git push origin main
```

---

## ⚠️ Importante: Variables de Entorno

### En Desarrollo (LOCAL)
El archivo `.env` contiene credenciales reales.

### En Producción
Crear un archivo `.env` diferente con:
```
DEBUG=False
SECRET_KEY=<generar_nueva_clave_segura>
DB_PASSWORD=<contraseña_producción>
ALLOWED_HOSTS=tudominio.com,www.tudominio.com
```

**NUNCA** incluir el `.env` de producción en Git.

---

## 🔍 Verificar que Todo Funciona

### Checklist Final

- [ ] `python manage.py runserver` funciona sin errores
- [ ] Login/logout funcionan sin 404
- [ ] Las listas (productos, clientes, pedidos) cargan sin errores
- [ ] Los formularios validan correctamente
- [ ] Los botones de acción solo aparecen si tienes permiso
- [ ] El `.env` contiene todas las variables necesarias
- [ ] El `.gitignore` contiene `.env`

### Comandos Útiles de Diagnóstico

```bash
# Ver configuración de base de datos
python manage.py shell
>>> from django.conf import settings
>>> print(settings.DATABASES)

# Ver ruta de login
python manage.py shell
>>> from django.urls import reverse
>>> print(reverse('login'))
>>> print(reverse('logout'))
>>> print(reverse('index'))

# Verificar que decouple funciona
python manage.py shell
>>> from decouple import config
>>> print(config('DEBUG'))
>>> print(config('DB_NAME'))
```

---

## 📞 Solución de Problemas

### Problema: "ModuleNotFoundError: No module named 'decouple'"
**Solución**: Ejecutar `pip install python-decouple`

### Problema: Variables de entorno no se cargan
**Solución**: Verificar que `.env` esté en la raíz del proyecto (mismo nivel que `manage.py`)

### Problema: Login redirige a 404
**Solución**: Verificar que en `settings.py` tengamos:
```python
LOGIN_URL = 'login'  # NO '/accounts/login/'
```

### Problema: Formulario no valida negativas
**Solución**: Ejecutar migraciones: `python manage.py migrate`

### Problema: Botones no aparecen en tabla
**Solución**: Limpiar caché del navegador (Ctrl+Shift+Delete) y recargar

---

## 📚 Documentación Referencia

- **REVISION.md** - Revisión completa del proyecto
- **ERRORES_IDENTIFICADOS.md** - Errores y soluciones
- **REFACTORIZACION.md** - Detalle de cambios (este documento)
- **README.md** - Descripción general del proyecto

---

## ✅ Resumen

Todos los cambios están implementados. Solo necesitas:

1. **Instalar dependencias**: `pip install python-decouple`
2. **Ejecutar migraciones**: `python manage.py migrate`
3. **Probar**: `python manage.py runserver`
4. **Subir**: `git push`

¡Listo para producción! 🚀

