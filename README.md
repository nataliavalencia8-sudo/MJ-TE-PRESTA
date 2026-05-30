# 💰 MJ TE PRESTA

Sistema Gestor de Préstamos — Universidad de Antioquia  
Facultad de Ingeniería | Curso: Algoritmia y Programación  
Profesora: Cindy Estrada

---

## 👥 Integrantes

| Nombre | Rol | Programa | Semestre |
|---|---|---|---|
| Manuela Bustamante Castrillón | Líder | Ingeniería Industrial | 3° |
| Fabian Saul Jimenez Madera | Desarrollador Backend | Ingeniería Industrial | 3° |
| Miguel Angel López Garcia | Desarrollador Backend | Ingeniería Industrial | 3° |
| Angie Natalia Valencia Castañeda | QA / Documentación | Ingeniería Industrial | 3° |

---

## 🎓 Vínculos Académicos y Descripción

**Manuela Bustamante** — Líder del proyecto. Estudiante de Ingeniería Industrial con interés en programación y desarrollo técnico. Dominio de Python, liderazgo y gestión de conflictos.

**Fabian Jimenez** — Desarrollador Backend. Enfoque metodológico y estructurado. Fortalezas en análisis cuantitativo y comunicación efectiva. Aplica Python en automatización y diseño de sistemas.

**Miguel Angel López** — Desarrollador Backend. Participa en programación estructurada, manejo de archivos planos y validación de datos. Responsable de la clase `clsUsuarios` y el módulo de devoluciones.

**Natalia Valencia** — QA y Documentación. Responsable del módulo administrador, manual de usuario y pruebas funcionales. Fortalezas en atención al detalle y redacción técnica.

---

## 📌 Nombre del Proyecto

**MJ TE PRESTA**

Sistema diseñado para ayudar a MJ a gestionar sus préstamos de artículos (juegos, herramientas, electrodomésticos y más) de forma digital, eliminando el problema del olvido.

---

## 📄 Licencia

[Ver licencia del proyecto](https://docs.google.com/document/d/1TPPEsn0r-WXXDK1196iyZ8XCS37p2OqnW6AvVWt2218/edit?usp=sharing)

---

## 🔭 Reporte de Visión

**MJ TE PRESTA** es un sistema en Python diseñado para que Michael Jackson Gamboa (MJ) administre de forma organizada el préstamo de sus artículos personales a sus amigos. Soluciona la pérdida de objetos y la falta de registros mediante la digitalización del proceso.

**Funcionalidades principales:**
- Registro de usuarios e ítems con códigos únicos
- Gestión de salidas y devoluciones
- Alertas automáticas de cobro a partir del día 20
- Generación de facturas con 23% de impuesto por retrasos mayores a 30 días
- Exportación de datos a CSV
- Trazabilidad completa y respaldo documental

---

## ⚙️ Especificación de Requisitos

### Requisitos Funcionales

**Gestión de Usuarios**
- Registro con nombre, apellido, documento, correo y plazo de préstamo
- Validaciones: nombres mín. 3 caracteres, documento 3–15 dígitos, formato de correo con `@` y `.com`
- Plazos de préstamo: 5, 10, 15 o 30 días

**Gestión de Ítems**
- Registro con nombre, categoría, valor, ID y estado
- Categorías: Videojuegos, Libros, Música y video, Herramientas, Dinero, Misceláneo
- Condición evaluada con lógica difusa: Excelente, Bueno, Regular, Malo

**Gestión de Préstamos**
- Solo para usuarios registrados
- Almacena fecha de inicio, datos del usuario, artículo y plazo
- Alertas automáticas desde el día 20

**Devoluciones y Certificados**
- Solo aplica para préstamos activos
- Verifica ítems pendientes antes de registrar devolución

**Facturación por Venta**
- Conversión automática a venta si el retraso supera 30 días
- Factura con subtotal + 23% de gravamen por demora

**Módulo Administrador**
- Autenticación con credenciales
- Informes de saldos, devoluciones, ventas y perfiles de usuarios

### Requisitos No Funcionales
- **Usabilidad:** Menú en español con mensajes de error descriptivos
- **Persistencia:** Datos en archivos planos `.txt` y `.csv`
- **Escalabilidad:** Soporte para mínimo 100 usuarios y 500 ítems

---

## 📅 Plan de Proyecto

| Actividad | Responsable | S1 (26/05–01/06) | S2 (02/06–08/06) | S3 (09/06–14/06) |
|---|---|:---:|:---:|:---:|
| Acta de entendimiento | Todos | ● | | |
| Acta de colaboración | Todos | ● | | |
| Acta de responsabilidad | Todos | ● | | |
| README y vínculos académicos | Manuela | ● | | |
| Nombre, licencia, reporte de visión | Fabián | ● | | |
| Especificación de requisitos | Miguel Ángel | ● | ● | |
| Plan de proyecto (Gantt) | Natalia | ● | | |
| Plan de versionado | Fabián | | ● | |
| Desarrollo clsUsuario | Manuela | | ● | ● |
| Desarrollo Préstamo | Fabián | | ● | ● |
| Módulo devolución y ventas | Miguel Ángel | | ● | ● |
| Módulo administrador y reportes | Natalia | | ● | ● |
| Manual de usuario | Natalia | | | ● |
| Pruebas y correcciones | Todos | | | ● |
| Entrega final GitHub | Manuela | | | ● |

### 💲 Presupuesto

| Integrante | Horas | Valor/hr | Total |
|---|---|---|---|
| Manuela Bustamante | 12–13 h | $5.682 | $73.866 |
| Fabián Jiménez | 12–13 h | $5.682 | $73.866 |
| Miguel Ángel | 12–13 h | $5.682 | $73.866 |
| Natalia Valencia | 12–13 h | $5.682 | $73.866 |
| **TOTAL** | **50 h** | — | **$284.100** |
