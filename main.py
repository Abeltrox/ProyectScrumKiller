# ==================================================
# MAIN - ECOMMERCE FRAMEWORK
# ==================================================

from services.auth_service import ServicioAutenticacion
from services.auth_user_service import ServicioAutenticacionUsuario
from services.product_service import ServicioProducto


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
# MENÚ USUARIO FINAL (COMPRADOR)
# ==================================================

def menu_usuario_final(servicio_usuario):

    while True:
        titulo("USUARIO FINAL")

        print("1. Registrarse")
        print("2. Iniciar sesión")
        print("3. Volver")
        linea()

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            titulo("REGISTRO DE USUARIO")

            nombre = input("Nombre: ")
            correo = input("Correo: ")
            contrasena = input("Contraseña: ")

            exito, mensaje = servicio_usuario.registrar_usuario(
                nombre, correo, contrasena
            )

            print("\n" + mensaje)

        elif opcion == "2":
            titulo("LOGIN USUARIO")

            correo = input("Correo: ")
            contrasena = input("Contraseña: ")

            exito, resultado = servicio_usuario.iniciar_sesion(
                correo, contrasena
            )

            if exito:
                titulo(f"Bienvenido {resultado['nombre']}")
            else:
                print("\n" + resultado)

        elif opcion == "3":
            break

        else:
            print("Opción inválida.")


# ==================================================
# MENÚ ADMINISTRADOR DE PRODUCTOS (TIENDA)
# ==================================================

def menu_admin_productos(servicio_producto, cliente):

    while True:
        titulo(f"PANEL ADMIN - {cliente['nombre']}")

        print("1. Crear producto")
        print("2. Ver mis productos")
        print("3. Volver")
        linea()

        opcion = input("Seleccione opción: ")

        # ------------------------------
        # CREAR PRODUCTO
        # ------------------------------
        if opcion == "1":
            titulo("CREAR PRODUCTO")

            try:
                nombre = input("Nombre producto: ")
                descripcion = input("Descripción: ")
                precio = float(input("Precio: "))
                moneda = input("Moneda (COP/USD/EUR): ")
                stock = int(input("Stock: "))
                categoria = input("Categoría: ")

                exito, mensaje = servicio_producto.crear_producto(
                    nombre,
                    descripcion,
                    precio,
                    moneda,
                    stock,
                    categoria,
                    cliente["id"]
                )

                print("\n" + mensaje)

            except ValueError:
                print("\nError: precio o stock inválido.")

        # ------------------------------
        # VER PRODUCTOS
        # ------------------------------
        elif opcion == "2":
            titulo("MIS PRODUCTOS")

            productos = servicio_producto.obtener_catalogo(cliente["id"])

            if not productos:
                print("No tienes productos registrados.")
            else:
                for p in productos:
                    print(f"""
ID: {p['id']}
Nombre: {p['nombre']}
Precio: {p['precio']} {p['moneda']}
Stock: {p['stock']}
Categoría: {p['categoria']}
---------------------------------------
""")

        elif opcion == "3":
            break

        else:
            print("Opción inválida.")


# ==================================================
# MENÚ PRINCIPAL
# ==================================================

def mostrar_menu_principal():
    titulo("E-COMMERCE FRAMEWORK")

    print("1. Registrar tienda")
    print("2. Iniciar sesión tienda")
    print("3. Usuario final")
    print("4. Salir")
    linea()


# ==================================================
# FUNCIÓN PRINCIPAL
# ==================================================

def main():

    servicio_auth = ServicioAutenticacion()
    servicio_usuario = ServicioAutenticacionUsuario()
    servicio_producto = ServicioProducto()

    while True:
        mostrar_menu_principal()
        opcion = input("Seleccione una opción: ")

        # ------------------------------
        # REGISTRO TIENDA
        # ------------------------------
        if opcion == "1":
            titulo("REGISTRO DE TIENDA")

            nombre = input("Nombre de la tienda: ")
            correo = input("Correo: ")
            contrasena = input("Contraseña: ")
            idioma = input("Idioma (es/en): ")

            resultado = servicio_auth.registrar_tienda(
                nombre,
                correo,
                contrasena,
                idioma
            )

            print("\n" + resultado)

        # ------------------------------
        # LOGIN TIENDA
        # ------------------------------
        elif opcion == "2":
            titulo("LOGIN TIENDA")

            correo = input("Correo: ")
            contrasena = input("Contraseña: ")

            exito, resultado = servicio_auth.iniciar_sesion(
                correo,
                contrasena
            )

            if exito:
                titulo(f"Bienvenido {resultado['nombre']}")
                menu_admin_productos(servicio_producto, resultado)
            else:
                print("\n" + resultado)

        # ------------------------------
        # USUARIO FINAL
        # ------------------------------
        elif opcion == "3":
            menu_usuario_final(servicio_usuario)

        # ------------------------------
        # SALIR
        # ------------------------------
        elif opcion == "4":
            print("\nSaliendo del sistema...")
            break

        else:
            print("Opción inválida.")


# ==================================================
# EJECUCIÓN
# ==================================================

if __name__ == "__main__":
    main()
