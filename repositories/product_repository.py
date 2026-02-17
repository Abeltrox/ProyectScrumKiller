import json
from config.settings import BASE_DIR

RUTA_PRODUCTOS = BASE_DIR / "database" / "productos.json"


class RepositorioProducto:

    def actualizar_producto(self, producto_actualizado):
        datos = self._leer_archivo()

        for i, producto in enumerate(datos["productos"]):
            if producto["id"] == producto_actualizado["id"]:
                datos["productos"][i] = producto_actualizado
                self._guardar_archivo(datos)
                return True

        return False

    def eliminar_producto(self, producto_id, client_id):
        datos = self._leer_archivo()

        for producto in datos["productos"]:
            if producto["id"] == producto_id and producto["client_id"] == client_id:
                datos["productos"].remove(producto)
                self._guardar_archivo(datos)
                return True

        return False



    def _leer_archivo(self):
        if not RUTA_PRODUCTOS.exists():
            return {"productos": []}

        try:
            with open(RUTA_PRODUCTOS, "r", encoding="utf-8") as archivo:
                return json.load(archivo)
        except Exception:
            return {"productos": []}

    def _guardar_archivo(self, datos):
        with open(RUTA_PRODUCTOS, "w", encoding="utf-8") as archivo:
            json.dump(datos, archivo, indent=4, ensure_ascii=False)

    def guardar_producto(self, producto_dict):
        datos = self._leer_archivo()
        datos["productos"].append(producto_dict)
        self._guardar_archivo(datos)

    def obtener_todos(self):
        datos = self._leer_archivo()
        return datos["productos"]

    def obtener_por_tienda(self, client_id):
        datos = self._leer_archivo()
        return [
            p for p in datos["productos"]
            if p["client_id"] == client_id
        ]

    def buscar_por_id(self, producto_id):
        datos = self._leer_archivo()
        for producto in datos["productos"]:
            if producto["id"] == producto_id:
                return producto
        return None
