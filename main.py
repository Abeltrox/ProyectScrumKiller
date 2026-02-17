from services.auth_service import ServicioAutenticacion


def main():

    servicio_auth = ServicioAutenticacion()

    print("---- REGISTRO DE TIENDA ----")
    resultado_registro = servicio_auth.registrar_tienda(
        nombre="Tech Store",
        correo="admin@tech.com",
        contrasena="123456",
        idioma="es"
    )
    print(resultado_registro)

    print("---- INICIO DE SESIÓN ----")
    resultado_login = servicio_auth.iniciar_sesion(
        correo="admin@tech.com",
        contrasena="123456"
    )
    print(resultado_login)


if __name__ == "__main__":
    main()
