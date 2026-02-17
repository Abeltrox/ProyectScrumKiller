import json
from config.settings import RUTA_BASEDATOS
from utils.logger import logger


class RepositorioCliente:

    def _leer_base_de_datos(self):
        try:
            with open(RUTA_BASEDATOS, "r") as archivo:
                return json.load(archivo)
        except:
            return {
                "clientes": [],
                "usuarios": [],
                "productos": [],
                "ordenes": []
            }

    def _escribir_base_de_datos(self, datos):
        with open(RUTA_BASEDATOS, "w") as archivo:
            json.dump(datos, archivo, indent=4)

    def guardar(self, cliente):
        datos = self._leer_base_de_datos()
        datos["clientes"].append(cliente.a_diccionario())
        self._escribir_base_de_datos(datos)
        logger.info("Cliente guardado correctamente")

    def buscar_por_correo(self, correo):
        datos = self._leer_base_de_datos()
        for cliente in datos["clientes"]:
            if cliente["correo"] == correo:
                return cliente
        return None

    def obtener_todos(self):
        datos = self._leer_base_de_datos()
        return datos["clientes"]