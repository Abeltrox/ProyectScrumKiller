# ==================================================
# MAIN - ECOMMERCE FRAMEWORK
# ==================================================

from services.auth_service import ServicioAutenticacion
from services.auth_user_service import ServicioAutenticacionUsuario
from services.product_service import ServicioProducto
from services.payment_service import ServicioPago
from services.order_service import ServicioOrdenes
from repositories.client_repository import RepositorioCliente
from utils.i18n import t
from services.checkout_service import procesar_checkout



# ==================================================
# UTILIDADES VISUALES
# ==================================================

def linea():
    print("=" * 55)


def titulo(texto):
    linea()
    print(texto.center(55))
    linea()


# ==================================================
# TAREA 8 - PAGO CON TARJETA SIMULADA
# ==================================================

def flujo_pago(servicio_pago, servicio_ordenes, usuario, carrito, idioma="es"):
    if not carrito:
        print("\nEl carrito está vacío." if idioma == "es" else "\nCart is empty.")
        return False

    total = sum(item["precio_unitario"] * item["cantidad"] for item in carrito)
    moneda = carrito[0]["moneda"]
    client_id = carrito[0]["client_id"]

    titulo(t("titulo_pago", idioma))
    print(f"Total: {total:.2f} {moneda}\n")

    numero_tarjeta = input(t("numero_tarjeta", idioma)).strip()
    nombre_titular = input(t("titular", idioma)).strip()
    mes_exp = input(t("mes_exp", idioma)).strip()
    anio_exp = input(t("anio_exp", idioma)).strip()
    cvv = input(t("cvv", idioma)).strip()

    exito, resultado = servicio_pago.procesar_pago(
        numero_tarjeta, nombre_titular, mes_exp, anio_exp, cvv, total, moneda
    )

    if not exito:
        print(f"\nPago rechazado: {resultado}" if idioma == "es" else f"\nPayment declined: {resultado}")
        return False

    orden = servicio_ordenes.crear_orden(
        usuario_id=usuario["id"],
        client_id=client_id,
        items=carrito,
        total=total,
        moneda=moneda,
        transaccion_id=resultado["transaccion_id"]
    )

    titulo(t("pago_exitoso", idioma))
    print(f"{t('transaccion_id', idioma)}: {resultado['transaccion_id']}")
    print(f"{t('tarjeta_termina', idioma)}: **** **** **** {resultado['tarjeta_terminada_en']}")
    print(f"{t('total', idioma)}: {total:.2f} {moneda}")
    print(f"{t('fecha', idioma)}: {resultado['fecha']}")
    print(f"Orden ID: {orden['id']}")
    return True

def flujo_checkout(servicio_pago, servicio_ordenes, usuario, carrito, idioma="es"):
    return procesar_checkout(
        servicio_pago,
        servicio_ordenes,
        usuario,
        carrito,
        idioma
    )

# ==================================================
# TAREA 9 - VER ORDENES USUARIO FINAL
# ==================================================

def ver_mis_ordenes(servicio_ordenes, usuario, idioma="es"):
    titulo(t("mis_ordenes_titulo", idioma))
    ordenes = servicio_ordenes.obtener_ordenes_usuario(usuario["id"])

    if not ordenes:
        print(t("no_mis_ordenes", idioma))
        return

    for orden in ordenes:
        linea()
        print(f"{t('orden_id', idioma)}: {orden['id']}")
        print(f"{t('fecha', idioma)}: {orden['fecha']}")
        print(f"{t('total', idioma)}: {orden['total']:.2f} {orden['moneda']}")
        print(f"{t('estado', idioma)}: {orden['estado']}")
        print(f"{t('items', idioma)}:")
        for item in orden["items"]:
            print(f"  - {item['nombre']} x{item['cantidad']} @ {item['precio_unitario']} {orden['moneda']}")
    linea()


# ==================================================
# TAREA 9 - VER ORDENES TIENDA (ADMIN)
# ==================================================

def ver_ordenes_tienda(servicio_ordenes, cliente, idioma="es"):
    titulo(t("ordenes_tienda", idioma))
    ordenes = servicio_ordenes.obtener_ordenes_tienda(cliente["id"])

    if not ordenes:
        print(t("no_ordenes", idioma))
        return

    for orden in ordenes:
        linea()
        print(f"{t('orden_id', idioma)}: {orden['id']}")
        print(f"{t('usuario', idioma)} ID: {orden['usuario_id']}")
        print(f"{t('fecha', idioma)}: {orden['fecha']}")
        print(f"{t('total', idioma)}: {orden['total']:.2f} {orden['moneda']}")
        print(f"{t('estado', idioma)}: {orden['estado']}")
        print(f"{t('items', idioma)}:")
        for item in orden["items"]:
            print(f"  - {item['nombre']} x{item['cantidad']} @ {item['precio_unitario']} {orden['moneda']}")
    linea()


# ==================================================
# TAREA 5 - CATALOGO + TAREA 8/9 - USUARIO LOGUEADO
# ==================================================

def menu_usuario_logueado(servicio_producto, servicio_pago, servicio_ordenes, usuario, idioma="es"):
    repo_cliente = RepositorioCliente()

    while True:
        titulo(f"{t('bienvenido', idioma)}, {usuario['nombre']}")
        print("1. " + ("Ver catalogo de tienda" if idioma == "es" else "View store catalog"))
        print("2. " + ("Ver mis ordenes" if idioma == "es" else "View my orders"))
        print("3. " + ("Volver" if idioma == "es" else "Back"))
        linea()

        opcion = input("Seleccione una opcion: " if idioma == "es" else "Select an option: ").strip()

        print(f"DEBUG - opcion ingresada: '{opcion}'")

        if opcion == "1":
            try:
                titulo("CATALOGO DE PRODUCTOS" if idioma == "es" else "PRODUCT CATALOG")
                tiendas = repo_cliente.obtener_todos()
                print(f"DEBUG - tiendas encontradas: {tiendas}")

                if not tiendas:
                    print("No hay tiendas registradas.")
                    continue

                print("Tiendas disponibles:" if idioma == "es" else "Available stores:")
                for i, tienda in enumerate(tiendas, 1):
                    print(f"  {i}. {tienda['nombre']}")
                linea()

                seleccion = int(input("Seleccione el numero de la tienda: ").strip()) - 1
                if seleccion < 0 or seleccion >= len(tiendas):
                    print("Seleccion invalida.")
                    continue
                client_id = tiendas[seleccion]["id"]

                productos = servicio_producto.obtener_catalogo(client_id)

                if not productos:
                    print("Esta tienda no tiene productos disponibles.")
                else:
                    for p in productos:
                        disponible = "OK" if p["stock"] > 0 else "AGOTADO"
                        print(f"\n[{disponible}] ID: {p['id']}")
                        print(f"    {p['nombre']} - {p['precio']} {p['moneda']}")
                        print(f"    {p['descripcion']}")
                        print(f"    Stock: {p['stock']} | Categoria: {p['categoria']}")
                    linea()

                    pagar = input("Desea comprar un producto? (s/n): " if idioma == "es" else "Do you want to buy? (y/n): ").strip().lower()
                    confirmar = "s" if idioma == "es" else "y"

                    if pagar == confirmar:
                        producto_id = input("ID del producto: ").strip()
                        producto = servicio_producto.buscar_producto(producto_id)

                        if not producto:
                            print("Producto no encontrado.")
                        elif producto["stock"] <= 0:
                            print("Producto sin stock.")
                        else:
                            try:
                                cantidad = int(input("Cantidad: ").strip())
                                if cantidad <= 0 or cantidad > producto["stock"]:
                                    print("Cantidad invalida.")
                                else:
                                    carrito = [{
                                        "producto_id": producto["id"],
                                        "nombre": producto["nombre"],
                                        "cantidad": cantidad,
                                        "precio_unitario": producto["precio"],
                                        "moneda": producto["moneda"],
                                        "client_id": producto["client_id"]
                                    }]
                                    flujo_checkout(servicio_pago, servicio_ordenes, usuario, carrito, idioma)
                            except ValueError:
                                print("Cantidad invalida.")

            except Exception as e:
                print(f"ERROR en catalogo: {e}")
                import traceback
                traceback.print_exc()

        elif opcion == "2":
            try:
                ver_mis_ordenes(servicio_ordenes, usuario, idioma)
            except Exception as e:
                print(f"ERROR en ordenes: {e}")
                import traceback
                traceback.print_exc()

        elif opcion == "3":
            break

        else:
            print(f"Opcion invalida. Recibido: '{opcion}'")


# ==================================================
# MENU USUARIO FINAL
# ==================================================

def menu_usuario_final(servicio_usuario, servicio_producto, servicio_pago, servicio_ordenes):
    while True:
        titulo("USUARIO FINAL")
        print("1. Registrarse")
        print("2. Iniciar sesion")
        print("3. Volver")
        linea()

        opcion = input("Seleccione una opcion: ").strip()

        if opcion == "1":
            titulo("REGISTRO DE USUARIO")
            nombre = input("Nombre: ")
            correo = input("Correo: ")
            contrasena = input("Contrasena: ")

            exito, mensaje = servicio_usuario.registrar_usuario(nombre, correo, contrasena)
            print("\n" + mensaje)

        elif opcion == "2":
            titulo("LOGIN USUARIO")
            correo = input("Correo: ")
            contrasena = input("Contrasena: ")

            exito, resultado = servicio_usuario.iniciar_sesion(correo, contrasena)

            if exito:
                menu_usuario_logueado(
                    servicio_producto, servicio_pago, servicio_ordenes,
                    resultado, idioma="es"
                )
            else:
                print("\n" + resultado)

        elif opcion == "3":
            break

        else:
            print("Opcion invalida.")


# ==================================================
# MENU ADMIN PRODUCTOS
# ==================================================

def menu_admin_productos(servicio_producto, servicio_ordenes, cliente):
    idioma = cliente.get("idioma", "es")

    while True:
        titulo(f"{t('panel_admin', idioma)} - {cliente['nombre']}")
        print("1. " + ("Crear producto" if idioma == "es" else "Create product"))
        print("2. " + ("Ver mis productos" if idioma == "es" else "View my products"))
        print("3. " + ("Actualizar producto" if idioma == "es" else "Update product"))
        print("4. " + ("Eliminar producto" if idioma == "es" else "Delete product"))
        print("5. " + ("Ver ordenes recibidas" if idioma == "es" else "View received orders"))
        print("6. " + ("Volver" if idioma == "es" else "Back"))
        linea()

        opcion = input("Seleccione una opcion: " if idioma == "es" else "Select an option: ").strip()

        if opcion == "1":
            titulo("CREAR PRODUCTO" if idioma == "es" else "CREATE PRODUCT")
            try:
                nombre = input("Nombre producto: " if idioma == "es" else "Product name: ")
                descripcion = input("Descripcion: " if idioma == "es" else "Description: ")
                precio = float(input("Precio: " if idioma == "es" else "Price: "))
                moneda = input("Moneda (COP/USD/EUR): " if idioma == "es" else "Currency (COP/USD/EUR): ")
                stock = int(input("Stock: "))
                categoria = input("Categoria: " if idioma == "es" else "Category: ")

                exito, mensaje = servicio_producto.crear_producto(
                    nombre, descripcion, precio, moneda, stock, categoria, cliente["id"]
                )
                print("\n" + mensaje)

            except ValueError:
                print("\nError: precio o stock invalido." if idioma == "es" else "\nError: invalid price or stock.")

        elif opcion == "2":
            titulo("MIS PRODUCTOS" if idioma == "es" else "MY PRODUCTS")
            productos = servicio_producto.obtener_catalogo(cliente["id"])

            if not productos:
                print("No tienes productos registrados." if idioma == "es" else "You have no registered products.")
            else:
                for p in productos:
                    print(f"\nID: {p['id']}")
                    print(f"{'Nombre' if idioma == 'es' else 'Name'}: {p['nombre']}")
                    print(f"{'Descripcion' if idioma == 'es' else 'Description'}: {p['descripcion']}")
                    print(f"{'Precio' if idioma == 'es' else 'Price'}: {p['precio']} {p['moneda']}")
                    print(f"Stock: {p['stock']}")
                    print(f"{'Categoria' if idioma == 'es' else 'Category'}: {p['categoria']}")
                    print("---------------------------------------")

        elif opcion == "3":
            titulo("ACTUALIZAR PRODUCTO" if idioma == "es" else "UPDATE PRODUCT")
            productos = servicio_producto.obtener_catalogo(cliente["id"])

            if not productos:
                print("No tienes productos registrados." if idioma == "es" else "You have no registered products.")
            else:
                for p in productos:
                    print(f"  ID: {p['id']} | {p['nombre']} | {p['precio']} {p['moneda']} | Stock: {p['stock']}")
                linea()

                producto_id = input("ID del producto a actualizar: " if idioma == "es" else "Product ID to update: ").strip()
                print("\nDeja en blanco los campos que no quieras cambiar." if idioma == "es" else "\nLeave blank fields you don't want to change.")

                datos_actualizados = {}

                v = input("Nuevo nombre: " if idioma == "es" else "New name: ").strip()
                if v: datos_actualizados["nombre"] = v

                v = input("Nueva descripcion: " if idioma == "es" else "New description: ").strip()
                if v: datos_actualizados["descripcion"] = v

                v = input("Nuevo precio: " if idioma == "es" else "New price: ").strip()
                if v:
                    try: datos_actualizados["precio"] = float(v)
                    except ValueError: print("Precio invalido, no se modificara.")

                v = input("Nueva moneda (COP/USD/EUR): " if idioma == "es" else "New currency: ").strip()
                if v: datos_actualizados["moneda"] = v

                v = input("Nuevo stock: " if idioma == "es" else "New stock: ").strip()
                if v:
                    try: datos_actualizados["stock"] = int(v)
                    except ValueError: print("Stock invalido, no se modificara.")

                v = input("Nueva categoria: " if idioma == "es" else "New category: ").strip()
                if v: datos_actualizados["categoria"] = v

                if datos_actualizados:
                    exito, mensaje = servicio_producto.actualizar_producto(producto_id, datos_actualizados, cliente["id"])
                    print("\n" + mensaje)
                else:
                    print("\nNo se realizaron cambios." if idioma == "es" else "\nNo changes made.")

        elif opcion == "4":
            titulo("ELIMINAR PRODUCTO" if idioma == "es" else "DELETE PRODUCT")
            productos = servicio_producto.obtener_catalogo(cliente["id"])

            if not productos:
                print("No tienes productos registrados." if idioma == "es" else "You have no registered products.")
            else:
                for p in productos:
                    print(f"  ID: {p['id']} | {p['nombre']} | Stock: {p['stock']}")
                linea()

                producto_id = input("ID del producto a eliminar: " if idioma == "es" else "Product ID to delete: ").strip()
                confirmar_char = "s" if idioma == "es" else "y"
                confirmacion = input(f"Estas seguro de eliminar '{producto_id}'? (s/n): " if idioma == "es" else f"Are you sure you want to delete '{producto_id}'? (y/n): ").lower().strip()

                if confirmacion == confirmar_char:
                    exito, mensaje = servicio_producto.eliminar_producto(producto_id, cliente["id"])
                    print("\n" + mensaje)
                else:
                    print("\nOperacion cancelada." if idioma == "es" else "\nOperation cancelled.")

        elif opcion == "5":
            ver_ordenes_tienda(servicio_ordenes, cliente, idioma)

        elif opcion == "6":
            break

        else:
            print("Opcion invalida." if idioma == "es" else "Invalid option.")


# ==================================================
# MENU PRINCIPAL
# ==================================================

def mostrar_menu_principal():
    titulo("E-COMMERCE FRAMEWORK")
    print("1. Registrar tienda")
    print("2. Iniciar sesion tienda")
    print("3. Usuario final")
    print("4. Salir")
    linea()


def main():
    servicio_auth = ServicioAutenticacion()
    servicio_usuario = ServicioAutenticacionUsuario()
    servicio_producto = ServicioProducto()
    servicio_pago = ServicioPago()
    servicio_ordenes = ServicioOrdenes()

    while True:
        mostrar_menu_principal()
        opcion = input("Seleccione una opcion: ").strip()

        if opcion == "1":
            titulo("REGISTRO DE TIENDA")
            nombre = input("Nombre de la tienda: ")
            correo = input("Correo: ")
            contrasena = input("Contrasena: ")
            idioma = input("Idioma (es/en): ").strip().lower()
            if idioma not in ["es", "en"]:
                idioma = "es"

            resultado = servicio_auth.registrar_tienda(nombre, correo, contrasena, idioma)
            print("\n" + resultado)

        elif opcion == "2":
            titulo("LOGIN TIENDA")
            correo = input("Correo: ")
            contrasena = input("Contrasena: ")

            exito, resultado = servicio_auth.iniciar_sesion(correo, contrasena)

            if exito:
                idioma = resultado.get("idioma", "es")
                titulo(f"{t('bienvenido', idioma)} {resultado['nombre']}")
                menu_admin_productos(servicio_producto, servicio_ordenes, resultado)
            else:
                print("\n" + resultado)

        elif opcion == "3":
            menu_usuario_final(servicio_usuario, servicio_producto, servicio_pago, servicio_ordenes)

        elif opcion == "4":
            print("\nSaliendo del sistema...")
            break

        else:
            print("Opcion invalida.")


if __name__ == "__main__":
    main()
    # Fin de main.py