# Cambios realizados en aspecto visual y carrito

## Cambios en el aspecto visual

- Se implementó una paleta de colores pastel tipo arcoíris en todo el sitio, incluyendo fondos, botones y tarjetas.
- Se crearon gradientes animados para el fondo principal y la barra de navegación.
- Todos los botones CRUD (Ver, Editar, Eliminar, Agregar, Pagar, etc.) ahora usan fondos degradados pastel, con texto centrado, altura y ancho uniforme, y letras en morado oscuro para mayor contraste.
- Se eliminaron bordes y fondos blancos de los botones para mantener la coherencia visual.
- Se ajustó el tamaño y alineación de los botones de acciones para que no se amontonen, usando flexbox y mayor separación entre ellos.
- Se agregó una clase especial para el contenedor de botones de acciones en las tablas, aumentando el padding para mejorar la separación visual.
- Se unificó el tamaño de las tarjetas de productos para que todas tengan la misma altura y el contenido esté alineado.
- Se mejoró la legibilidad de los textos principales, aumentando el tamaño y el contraste.
- Se aplicó la misma lógica de diseño pastel a los botones de agregar al carrito y pagar.

## Cambios en el carrito de compras

- Se implementó un sistema de carrito basado en la sesión del usuario, permitiendo agregar productos desde la vista de detalle.
- Si el usuario no está autenticado, al intentar agregar al carrito se redirige a la página de login.
- El carrito almacena productos y cantidades, y permite ver un resumen con subtotales y total general.
- Se agregó una página dedicada para visualizar el carrito, con opción de eliminar productos y proceder al pago.
- Se añadió un indicador de cantidad de productos en el carrito dentro de la barra de navegación.
- Se crearon vistas y URLs para agregar, ver y eliminar productos del carrito.
- Se adaptaron los estilos de los botones del carrito para que coincidan con la paleta pastel general del sitio.

## Notas adicionales

- Todos los cambios de aspecto se realizaron en los archivos `estilos.css` y `estilos.min.css`.
- Los cambios de funcionalidad del carrito se implementaron en los archivos de vistas, URLs y plantillas correspondientes.
- Se recomienda limpiar la caché del navegador para ver correctamente los cambios visuales.
