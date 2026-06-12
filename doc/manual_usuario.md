# 📖 Manual de Usuario — MJ TE PRESTA

**Sistema:** MJ TE PRESTA  
**Versión:** 1.0  
**Curso:** Algoritmia y Programación — Universidad de Antioquia  

---

## ¿Cómo ejecutar el programa?

1. Tener instalado **Python 3.8 o superior**
2. Abrir una terminal en la carpeta `src/`
3. Ejecutar el comando:

```
python main.py
```

---

## Menú principal

Al iniciar el programa verá el siguiente menú:

```
1. Registrar Usuario
2. Registrar Ítem
3. Registrar Préstamo
4. Registrar Devolución
5. Consultar Ítems con más de 30 días
6. Consultar Artículos Prestados
7. Administrador
8. Salir
```

---

## 1. Registrar Usuario

Permite agregar un nuevo amigo al sistema.

**Datos requeridos:**
- **Nombre:** mínimo 3 letras, sin números
- **Apellido:** mínimo 3 letras, sin números
- **Documento:** solo números, entre 3 y 15 dígitos
- **Correo:** debe contener `@` y `.com`
- **Plazo de préstamo:** solo se permiten 5, 10, 15 o 30 días

---

## 2. Registrar Ítem

Permite agregar un objeto al inventario de MJ.

**Datos requeridos:**
- **Nombre:** mínimo 3 caracteres
- **Categoría:** elegir entre Videojuegos, Libros, Música y video, Herramientas, Dinero, Misceláneo
- **Precio de compra**
- **Estado:** Excelente, Bueno, Regular o Malo

El sistema genera automáticamente un ID único basado en la categoría (ej: `VJ001` para videojuegos).

---

## 3. Registrar Préstamo

Permite registrar el préstamo de un ítem a un usuario.

**Pasos:**
1. Ingresar el documento del usuario (debe estar registrado)
2. Ver el listado de ítems disponibles
3. Ingresar el ID del ítem a prestar

> ⚠️ Si el usuario no está registrado, el sistema lo informará y pedirá registrarlo primero.

---

## 4. Registrar Devolución

Permite registrar la devolución de un ítem prestado.

**Pasos:**
1. Ingresar el documento del usuario
2. Seleccionar el préstamo a devolver de la lista
3. El sistema genera automáticamente un **certificado de devolución** en la carpeta `data/`

> ⚠️ Solo se pueden registrar devoluciones de préstamos activos.

---

## 5. Consultar Ítems con más de 30 días

Muestra los ítems que llevan más de 30 días prestados y que deben ser facturados como venta.

---

## 6. Consultar Artículos Prestados

Muestra todos los préstamos activos ordenados de mayor a menor cantidad de días. Incluye alertas para préstamos de 20 o más días.

| Símbolo | Significado |
|---|---|
| ⚠️ | El ítem lleva 20 o más días prestado |
| 🔴 | El ítem lleva más de 30 días (debe venderse) |

---

## 7. Administrador

Acceso restringido con usuario y contraseña.

**Reportes disponibles:**
- Total de préstamos registrados
- Total de ítems devueltos
- Total de ventas realizadas
- Total de dinero recaudado
- Lista de usuarios
- Usuario con mayor y menor cantidad de préstamos
- Generación de facturas para préstamos vencidos (+30 días)

Las facturas se generan automáticamente en la carpeta `data/` con el nombre `factura_NombreUsuario_IDItem.txt`.

---

## Archivos generados por el sistema

Todos los archivos se guardan en la carpeta `data/`:

| Archivo | Descripción |
|---|---|
| `usuarios.csv` | Base de datos de usuarios |
| `items.csv` | Inventario de ítems |
| `prestamos.csv` | Registro de préstamos |
| `certificado_*.txt` | Certificados de devolución |
| `factura_*.txt` | Facturas de venta |

---

## Solución de problemas frecuentes

**"Usuario no encontrado"** → El usuario debe registrarse primero en la opción 1.

**"Ítem no disponible"** → El ítem ya está prestado. Espere a que sea devuelto.

**"No tiene préstamos activos"** → El usuario no tiene préstamos vigentes para devolver.
