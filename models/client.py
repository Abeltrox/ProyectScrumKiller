import uuid


class Cliente:
    def __init__(self, nombre, correo, contrasena, idioma="es"):
        self.id = str(uuid.uuid4())
        self.nombre = nombre
        self.correo = correo
        self.contrasena = contrasena
        self.idioma = idioma

    def a_diccionario(self):
        return {
            "id": self.id,
            "nombre": self.nombre,
            "correo": self.correo,
            "contrasena": self.contrasena,
            "idioma": self.idioma
        }
