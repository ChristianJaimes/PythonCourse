# MLTrack

MLTrack es una aplicación en Python para la gestión de un mercado virtual sencillo. Permite a usuarios con rol de **comprador** o **vendedor** interactuar con productos, pedidos y usuarios de forma modular y robusta.

---

## Características

- Registro e inicio de sesión con roles diferenciados (comprador o vendedor).
- Compradores pueden:
  - Ver productos disponibles.
  - Realizar pedidos.
  - Consultar historial de pedidos.
- Vendedores pueden:
  - Agregar, editar y eliminar productos.
  - Ver pedidos recibidos.
- Datos almacenados en archivos JSON para persistencia simple.
- Interfaz de consola modular y fácil de usar.

---

## Estructura de archivos

data/
├── usuarios.json
├── productos.json
└── pedidos.json
comprador.py
vendedor.py
utils.py
main.py

- `data/`: Carpeta donde se guardan los datos en formato JSON.
- `comprador.py`: Funciones y menú para usuarios compradores.
- `vendedor.py`: Funciones y menú para usuarios vendedores.
- `utils.py`: Funciones auxiliares para gestión de usuarios (registro, login).
- `main.py`: Punto de entrada principal que une todos los módulos.

---

## Requisitos

- Python 3.x
- No requiere librerías externas (usa solo librerías estándar).

---

## Cómo ejecutar

1. Clona o descarga el proyecto.
2. Asegúrate de tener la carpeta `data/` con los archivos JSON vacíos:
   - `usuarios.json` con contenido `[]`
   - `productos.json` con contenido `[]`
   - `pedidos.json` con contenido `[]`
3. Desde la terminal, en la carpeta del proyecto, ejecuta:

```bash
python main.py
Sigue las instrucciones en pantalla para registrar usuarios, iniciar sesión y usar las funcionalidades según tu rol.

Próximos pasos y mejoras
Implementar interfaz gráfica.

Mejorar la gestión de stock y validaciones.

Agregar búsqueda avanzada de productos.

Añadir reportes y estadísticas.

Autor

Kevin vergara
Dayner Osorio
Breyner Ruiz
 - Proyecto de Ingeniería de Software
```
