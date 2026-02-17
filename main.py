from services.auth_service import ServicioAutenticacion


def mostrar_menu():
    print("\n===== E-COMMERCE FRAMEWORK =====")
    print("1. Registrar tienda")
    print("2. Iniciar sesión")
    print("3. Salir")


def main():

    servicio_auth = ServicioAutenticacion()

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            print("\n--- REGISTRO DE TIENDA ---")
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

            print(resultado)

        elif opcion == "2":
            print("\n--- INICIO DE SESIÓN ---")
            correo = input("Correo: ")
            contrasena = input("Contraseña: ")

            resultado = servicio_auth.iniciar_sesion(
                correo,
                contrasena
            )

            print(resultado)

            if resultado == "Inicio de sesión exitoso":
                print("Bienvenido al panel de administración de la tienda.")

        elif opcion == "3":
            print("Saliendo del sistema...")
            break

        else:
            print("Opción inválida, intente nuevamente.")


if __name__ == "__main__":
    main()
