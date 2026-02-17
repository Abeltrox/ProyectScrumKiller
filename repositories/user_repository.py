from config.settings import RUTA_USUARIOS 
import json


class RepositorioUsuario:

    def _leer_archivo(self):
        if not RUTA_USUARIOS.exists():
            return {"usuarios": []}

        try:
            with open(RUTA_USUARIOS, "r", encoding="utf-8") as archivo:
                return json.load(archivo)
        except Exception:
            return {"usuarios": []}

    def _guardar_archivo(self, datos):
        with open(RUTA_USUARIOS, "w", encoding="utf-8") as archivo:
            json.dump(datos, archivo, indent=4, ensure_ascii=False)

    def guardar_usuario(self, usuario_dict):
        datos = self._leer_archivo()
        datos["usuarios"].append(usuario_dict)
        self._guardar_archivo(datos)

    def buscar_por_correo(self, correo):
        datos = self._leer_archivo()
        for usuario in datos["usuarios"]:
            if usuario["correo"] == correo:
                return usuario
        return None

    def obtener_todos(self):
        datos = self._leer_archivo()
        return datos["usuarios"]
