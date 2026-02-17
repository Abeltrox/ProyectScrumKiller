from models.client import Cliente
from repositories.client_repository import RepositorioCliente
from utils.hash_utils import encriptar_contrasena, verificar_contrasena
from utils.logger import logger


class ServicioAutenticacion:

    def __init__(self):
        self.repositorio_cliente = RepositorioCliente()

    # ✅ TAREA 1 – Registro de tienda
    def registrar_tienda(self, nombre, correo, contrasena, idioma="es"):

        cliente_existente = self.repositorio_cliente.buscar_por_correo(correo)

        if cliente_existente:
            logger.warning("Intento de registro con correo ya existente")
            return "La tienda ya está registrada"

        contrasena_encriptada = encriptar_contrasena(contrasena)

        cliente = Cliente(nombre, correo, contrasena_encriptada, idioma)
        self.repositorio_cliente.guardar(cliente)

        logger.info("Tienda registrada exitosamente")
        return "Tienda registrada exitosamente"

    # ✅ TAREA 2 – Login del cliente
    def iniciar_sesion(self, correo, contrasena):

        cliente = self.repositorio_cliente.buscar_por_correo(correo)

        if not cliente:
            logger.warning("Cliente no encontrado")
            return False, "Cliente no encontrado"

        if not verificar_contrasena(contrasena, cliente["contrasena"]):
            logger.warning("Contraseña incorrecta")
            return False, "Credenciales inválidas"

        logger.info("Inicio de sesión exitoso")
        return True, cliente
