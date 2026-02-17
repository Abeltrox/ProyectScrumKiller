import json
from config.settings import BASE_DIR

RUTA_PRODUCTOS = BASE_DIR / "database" / "productos.json"


class RepositorioProducto:

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
