# ==============================
# MAIN - ECOMMERCE FRAMEWORK
# ==============================

from services.auth_service import ServicioAutenticacion
from services.auth_user_service import ServicioAutenticacionUsuario


# ==============================
# FUNCIONES DE MENÚ
# ==============================

def linea():
    print("=" * 50)


def mostrar_menu_principal():
    linea()
    print("        E-COMMERCE FRAMEWORK")
    linea()
    print("1. Registrar tienda")
    print("2. Iniciar sesión tienda")
    print("3. Usuario final")
    print("4. Salir")
    linea()


def menu_usuario_final(servicio_usuario):
    """
    Menú para registro e inicio de sesión
    de usuarios finales (compradores)
    """
    while True:
        linea()
        print("          USUARIO FINAL")
        linea()
        print("1. Registrarse")
        print("2. Iniciar sesión")
        print("3. Volver")
        linea()

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            print("\n--- REGISTRO DE USUARIO ---")
            nombre = input("Nombre: ")
            correo = input("Correo: ")
            contrasena = input("Contraseña: ")

            exito, mensaje = servicio_usuario.registrar_usuario(
                nombre,
                correo,
                contrasena
            )

            print(f"\n{mensaje}")

        elif opcion == "2":
            print("\n--- INICIO DE SESIÓN USUARIO ---")
            correo = input("Correo: ")
            contrasena = input("Contraseña: ")

            exito, resultado = servicio_usuario.iniciar_sesion(
                correo,
                contrasena
            )

            if exito:
                linea()
                print(f" Bienvenido {resultado['nombre']} ")
                linea()
            else:
                print(f"\n{resultado}")

        elif opcion == "3":
            break

        else:
            print("Opción inválida.")


# ==============================
# FUNCIÓN PRINCIPAL
# ==============================

def main():

    # Instancias de servicios
    servicio_auth = ServicioAutenticacion()
    servicio_usuario = ServicioAutenticacionUsuario()

    while True:
        mostrar_menu_principal()
        opcion = input("Seleccione una opción: ")

        # ------------------------------
        # REGISTRO DE TIENDA
        # ------------------------------
        if opcion == "1":
            linea()
            print("      REGISTRO DE TIENDA")
            linea()

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

            print(f"\n{resultado}")

        # ------------------------------
        # LOGIN DE TIENDA
        # ------------------------------
        elif opcion == "2":
            linea()
            print("     INICIO DE SESIÓN TIENDA")
            linea()

            correo = input("Correo: ")
            contrasena = input("Contraseña: ")

            resultado = servicio_auth.iniciar_sesion(
                correo,
                contrasena
            )

            print(f"\n{resultado}")

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
            print("Opción inválida, intente nuevamente.")


# ==============================
# EJECUCIÓN
# ==============================

if __name__ == "__main__":
    main()
