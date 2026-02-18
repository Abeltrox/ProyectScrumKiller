# 🛒 There's No Business Like E-Business.

Un sistema de e-commerce por consola desarrollado en Python, que permite gestionar tiendas, productos, usuarios finales, carritos de compra, pagos simulados y órdenes.

---

## 📋 Descripción

**There's No Business Like E-Business.** es un framework de comercio electrónico orientado a consola que soporta dos tipos de actores: **tiendas (administradores)** y **usuarios finales (compradores)**. El sistema cuenta con autenticación segura, gestión de catálogos por tienda, flujo de pago con tarjeta simulada, y registro de órdenes persistente en archivos JSON.

---

## 🚀 Características

- **Registro e inicio de sesión** para tiendas y usuarios finales con contraseñas encriptadas.
- **Panel de administración** para que las tiendas gestionen su catálogo de productos (crear, leer, actualizar, eliminar).
- **Catálogo de productos** por tienda con información de stock, precio y categoría.
- **Carrito de compra** y flujo de pago simulado con tarjeta de crédito.
- **Gestión de órdenes**: los usuarios pueden ver su historial, y las tiendas pueden ver las órdenes recibidas.
- **Soporte multilenguaje** (español e inglés) configurable por tienda.
- **Persistencia de datos** en archivos JSON locales.
- **Logger** integrado para registro de eventos del sistema.

---

## 🗂️ Estructura del Proyecto

```
ProyectScrumKiller-develop/
│
├── main.py                    # Punto de entrada, menús y flujos principales
├── config/
│   └── settings.py            # Rutas base y configuración global
├── models/
│   ├── client.py              # Modelo de tienda/cliente
│   ├── user.py                # Modelo de usuario final
│   └── product.py             # Modelo de producto
├── repositories/
│   ├── client_repository.py   # Acceso a datos de tiendas
│   ├── user_repository.py     # Acceso a datos de usuarios
│   ├── product_repository.py  # Acceso a datos de productos
│   └── cart_repository.py     # Acceso a datos del carrito
├── services/
│   ├── auth_service.py        # Registro e inicio de sesión de tiendas
│   ├── auth_user_service.py   # Registro e inicio de sesión de usuarios
│   ├── product_service.py     # Lógica de gestión de productos
│   ├── cart_service.py        # Lógica del carrito de compra
│   ├── checkout_service.py    # Lógica del proceso de checkout
│   ├── payment_service.py     # Procesamiento de pagos simulados
│   └── order_service.py       # Gestión de órdenes
├── utils/
│   ├── hash_utils.py          # Encriptación y verificación de contraseñas
│   ├── i18n.py                # Internacionalización (es/en)
│   └── logger.py              # Logger del sistema
└── database/
    ├── archivo.json           # Base de datos de tiendas/clientes
    ├── usuarios.json          # Base de datos de usuarios finales
    ├── productos.json         # Base de datos de productos
    └── ordenes.json           # Base de datos de órdenes
```

---

## ⚙️ Requisitos

- Python 3.8 o superior
- No requiere dependencias externas (usa únicamente la biblioteca estándar de Python)

---

## ▶️ Instalación y Uso

1. **Clona el repositorio:**
   ```bash
   git clone https://github.com/tu-usuario/ProyectScrumKiller.git
   cd ProyectScrumKiller-develop
   ```

2. **Ejecuta el programa:**
   ```bash
   python main.py
   ```

3. **Navega por el menú principal:**
   ```
   =======================================================
                    E-COMMERCE FRAMEWORK
   =======================================================
   1. Registrar tienda
   2. Iniciar sesion tienda
   3. Usuario final
   4. Salir
   ```

---

## 🔄 Flujos Principales

### Como Tienda (Administrador)
1. Registrar tienda con nombre, correo, contraseña e idioma (es/en).
2. Iniciar sesión para acceder al panel de administración.
3. Gestionar el catálogo: crear, ver, actualizar y eliminar productos.
4. Consultar las órdenes recibidas de los compradores.

### Como Usuario Final
1. Registrarse con nombre, correo y contraseña.
2. Iniciar sesión para explorar el catálogo de tiendas disponibles.
3. Seleccionar una tienda, elegir un producto y definir la cantidad.
4. Completar el pago simulado con datos de tarjeta de crédito.
5. Ver el historial de órdenes propias.

---

## 💳 Pago Simulado

El módulo de pagos solicita los siguientes datos de tarjeta:
- Número de tarjeta
- Nombre del titular
- Mes y año de expiración
- CVV

Al completarse exitosamente, se genera una orden con ID de transacción, últimos 4 dígitos de la tarjeta, total, moneda y fecha.

---

## 🌐 Multilenguaje

El sistema soporta **español (es)** e **inglés (en)**. El idioma se configura al momento de registrar la tienda y afecta todos los mensajes del panel de administración y la experiencia del usuario.

---

## 📦 Modelos de Datos

### Producto
| Campo | Tipo | Descripción |
|---|---|---|
| id | string | Identificador único |
| nombre | string | Nombre del producto |
| descripcion | string | Descripción detallada |
| precio | float | Precio unitario |
| moneda | string | COP / USD / EUR |
| stock | int | Unidades disponibles |
| categoria | string | Categoría del producto |
| client_id | string | ID de la tienda propietaria |

### Orden
| Campo | Tipo | Descripción |
|---|---|---|
| id | string | Identificador único |
| usuario_id | string | ID del comprador |
| client_id | string | ID de la tienda |
| items | list | Productos comprados |
| total | float | Monto total |
| moneda | string | Moneda de la transacción |
| transaccion_id | string | ID del pago |
| fecha | string | Fecha de creación |
| estado | string | Estado de la orden |

---

## 🔐 Seguridad

Las contraseñas son almacenadas de forma encriptada mediante `hash_utils.py`. El sistema valida credenciales en cada inicio de sesión sin exponer contraseñas en texto plano.

---

## 📝 Licencia

Este proyecto fue desarrollado como parte de un proyecto académico/scrum. Libre para uso educativo.
