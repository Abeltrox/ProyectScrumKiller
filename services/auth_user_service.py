import uuid
from models.user import Usuario
from repositories.user_repository import RepositorioUsuario
from utils.hash_utils import encriptar_contrasena, verificar_contrasena


class ServicioAutenticacionUsuario:

    def __init__(self):
        self.repositorio = RepositorioUsuario()

    def registrar_usuario(self, nombre, correo, contrasena):
        # Verificar si el correo ya existe
        usuario_existente = self.repositorio.buscar_por_correo(correo)
        if usuario_existente:
            return False, "El correo ya está registrado."

        # Generar ID único
        user_id = str(uuid.uuid4())[:8]

        # Encriptar contraseña
        contrasena_hash = encriptar_contrasena(contrasena)

        # Crear objeto usuario
        usuario = Usuario(user_id, nombre, correo, contrasena_hash)

        # Guardar en repositorio
        self.repositorio.guardar_usuario(usuario.to_dict())

        return True, "Usuario registrado correctamente."

    def iniciar_sesion(self, correo, contrasena):
        usuario = self.repositorio.buscar_por_correo(correo)

        if not usuario:
            return False, "Usuario no encontrado."

        if not verificar_contrasena(contrasena, usuario["contrasena_hash"]):
            return False, "Contraseña incorrecta."

        return True, usuario
