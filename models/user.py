class Usuario:
    def __init__(self, id, nombre, correo, contrasena_hash):
        self.id = id
        self.nombre = nombre
        self.correo = correo
        self.contrasena_hash = contrasena_hash

    def to_dict(self):
        return {
            "id": self.id,
            "nombre": self.nombre,
            "correo": self.correo,
            "contrasena_hash": self.contrasena_hash
        }
