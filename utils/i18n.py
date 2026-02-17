# ==============================
# TAREA 10 - Cambio de idioma (i18n)
# ==============================

TRADUCCIONES = {
    "es": {
        # Menú principal
        "menu_titulo": "E-COMMERCE FRAMEWORK",
        "menu_registrar_tienda": "1. Registrar tienda",
        "menu_login_tienda": "2. Iniciar sesión tienda",
        "menu_usuario_final": "3. Usuario final",
        "menu_salir": "4. Salir",
        "seleccione_opcion": "Seleccione una opción: ",
        "opcion_invalida": "Opción inválida.",
        "saliendo": "Saliendo del sistema...",

        # Auth tienda
        "registro_tienda": "REGISTRO DE TIENDA",
        "login_tienda": "LOGIN TIENDA",
        "nombre_tienda": "Nombre de la tienda: ",
        "correo": "Correo: ",
        "contrasena": "Contraseña: ",
        "idioma": "Idioma (es/en): ",
        "bienvenido": "Bienvenido",

        # Panel admin
        "panel_admin": "PANEL ADMIN",
        "crear_producto": "1. Crear producto",
        "ver_productos": "2. Ver mis productos",
        "actualizar_producto": "3. Actualizar producto",
        "eliminar_producto": "4. Eliminar producto",
        "ver_ordenes_tienda": "5. Ver órdenes recibidas",
        "volver": "6. Volver",
        "nombre_producto": "Nombre producto: ",
        "descripcion": "Descripción: ",
        "precio": "Precio: ",
        "moneda_input": "Moneda (COP/USD/EUR): ",
        "stock": "Stock: ",
        "categoria": "Categoría: ",
        "no_productos": "No tienes productos registrados.",
        "mis_productos": "MIS PRODUCTOS",
        "titulo_crear": "CREAR PRODUCTO",
        "titulo_actualizar": "ACTUALIZAR PRODUCTO",
        "titulo_eliminar": "ELIMINAR PRODUCTO",
        "id_actualizar": "ID del producto a actualizar: ",
        "id_eliminar": "ID del producto a eliminar: ",
        "dejar_blanco": "Deja en blanco los campos que no quieras cambiar.",
        "nuevo_nombre": "Nuevo nombre: ",
        "nueva_desc": "Nueva descripción: ",
        "nuevo_precio": "Nuevo precio: ",
        "nueva_moneda": "Nueva moneda (COP/USD/EUR): ",
        "nuevo_stock": "Nuevo stock: ",
        "nueva_categoria": "Nueva categoría: ",
        "sin_cambios": "No se realizaron cambios.",
        "confirmar_eliminar": "¿Estás seguro de eliminar el producto '{}'? (s/n): ",
        "cancelado": "Operación cancelada.",
        "precio_invalido": "Precio inválido, no se modificará.",
        "stock_invalido": "Stock inválido, no se modificará.",
        "error_precio_stock": "Error: precio o stock inválido.",

        # Órdenes tienda
        "ordenes_tienda": "ÓRDENES RECIBIDAS",
        "no_ordenes": "No hay órdenes registradas.",
        "orden_id": "Orden ID",
        "usuario": "Usuario",
        "total": "Total",
        "fecha": "Fecha",
        "estado": "Estado",
        "items": "Productos",

        # Usuario final
        "usuario_final": "USUARIO FINAL",
        "registrarse": "1. Registrarse",
        "iniciar_sesion": "2. Iniciar sesión",
        "registro_usuario": "REGISTRO DE USUARIO",
        "login_usuario": "LOGIN USUARIO",
        "nombre": "Nombre: ",

        # Catálogo
        "ver_catalogo": "3. Ver catálogo de tienda",
        "mis_ordenes": "4. Ver mis órdenes",
        "pagar": "5. Realizar pago",
        "catalogo_titulo": "CATÁLOGO DE PRODUCTOS",
        "ingrese_id_tienda": "Ingrese ID de la tienda: ",
        "catalogo_vacio": "Esta tienda no tiene productos disponibles.",

        # Pago
        "titulo_pago": "PAGO CON TARJETA",
        "numero_tarjeta": "Número de tarjeta (16 dígitos): ",
        "titular": "Nombre del titular: ",
        "mes_exp": "Mes de expiración (MM): ",
        "anio_exp": "Año de expiración (AAAA): ",
        "cvv": "CVV: ",
        "monto": "Monto a pagar: ",
        "moneda_pago": "Moneda: ",
        "pago_exitoso": "¡PAGO APROBADO!",
        "transaccion_id": "ID Transacción",
        "tarjeta_termina": "Tarjeta terminada en",

        # Mis órdenes
        "mis_ordenes_titulo": "MIS ÓRDENES",
        "no_mis_ordenes": "No tienes órdenes registradas.",
    },

    "en": {
        # Main menu
        "menu_titulo": "E-COMMERCE FRAMEWORK",
        "menu_registrar_tienda": "1. Register store",
        "menu_login_tienda": "2. Store login",
        "menu_usuario_final": "3. End user",
        "menu_salir": "4. Exit",
        "seleccione_opcion": "Select an option: ",
        "opcion_invalida": "Invalid option.",
        "saliendo": "Exiting the system...",

        # Store auth
        "registro_tienda": "STORE REGISTRATION",
        "login_tienda": "STORE LOGIN",
        "nombre_tienda": "Store name: ",
        "correo": "Email: ",
        "contrasena": "Password: ",
        "idioma": "Language (es/en): ",
        "bienvenido": "Welcome",

        # Admin panel
        "panel_admin": "ADMIN PANEL",
        "crear_producto": "1. Create product",
        "ver_productos": "2. View my products",
        "actualizar_producto": "3. Update product",
        "eliminar_producto": "4. Delete product",
        "ver_ordenes_tienda": "5. View received orders",
        "volver": "6. Back",
        "nombre_producto": "Product name: ",
        "descripcion": "Description: ",
        "precio": "Price: ",
        "moneda_input": "Currency (COP/USD/EUR): ",
        "stock": "Stock: ",
        "categoria": "Category: ",
        "no_productos": "You have no registered products.",
        "mis_productos": "MY PRODUCTS",
        "titulo_crear": "CREATE PRODUCT",
        "titulo_actualizar": "UPDATE PRODUCT",
        "titulo_eliminar": "DELETE PRODUCT",
        "id_actualizar": "Product ID to update: ",
        "id_eliminar": "Product ID to delete: ",
        "dejar_blanco": "Leave blank the fields you don't want to change.",
        "nuevo_nombre": "New name: ",
        "nueva_desc": "New description: ",
        "nuevo_precio": "New price: ",
        "nueva_moneda": "New currency (COP/USD/EUR): ",
        "nuevo_stock": "New stock: ",
        "nueva_categoria": "New category: ",
        "sin_cambios": "No changes made.",
        "confirmar_eliminar": "Are you sure you want to delete product '{}'? (y/n): ",
        "cancelado": "Operation cancelled.",
        "precio_invalido": "Invalid price, it will not be modified.",
        "stock_invalido": "Invalid stock, it will not be modified.",
        "error_precio_stock": "Error: invalid price or stock.",

        # Store orders
        "ordenes_tienda": "RECEIVED ORDERS",
        "no_ordenes": "No orders registered.",
        "orden_id": "Order ID",
        "usuario": "User",
        "total": "Total",
        "fecha": "Date",
        "estado": "Status",
        "items": "Products",

        # End user
        "usuario_final": "END USER",
        "registrarse": "1. Register",
        "iniciar_sesion": "2. Login",
        "registro_usuario": "USER REGISTRATION",
        "login_usuario": "USER LOGIN",
        "nombre": "Name: ",

        # Catalog
        "ver_catalogo": "3. View store catalog",
        "mis_ordenes": "4. View my orders",
        "pagar": "5. Make a payment",
        "catalogo_titulo": "PRODUCT CATALOG",
        "ingrese_id_tienda": "Enter store ID: ",
        "catalogo_vacio": "This store has no available products.",

        # Payment
        "titulo_pago": "CARD PAYMENT",
        "numero_tarjeta": "Card number (16 digits): ",
        "titular": "Cardholder name: ",
        "mes_exp": "Expiration month (MM): ",
        "anio_exp": "Expiration year (YYYY): ",
        "cvv": "CVV: ",
        "monto": "Amount to pay: ",
        "moneda_pago": "Currency: ",
        "pago_exitoso": "PAYMENT APPROVED!",
        "transaccion_id": "Transaction ID",
        "tarjeta_termina": "Card ending in",

        # My orders
        "mis_ordenes_titulo": "MY ORDERS",
        "no_mis_ordenes": "You have no registered orders.",
    }
}


def t(clave, idioma="es"):
    """Retorna el texto traducido según el idioma del usuario/cliente."""
    idioma = idioma if idioma in TRADUCCIONES else "es"
    return TRADUCCIONES[idioma].get(clave, clave)
