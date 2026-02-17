import json
import uuid
from datetime import datetime
from config.settings import BASE_DIR

RUTA_ORDENES = BASE_DIR / "database" / "ordenes.json"


class ServicioOrdenes:

    def _leer_archivo(self):
        if not RUTA_ORDENES.exists():
            return {"ordenes": []}
        try:
            with open(RUTA_ORDENES, "r", encoding="utf-8") as archivo:
                return json.load(archivo)
        except Exception:
            return {"ordenes": []}

    def _guardar_archivo(self, datos):
        with open(RUTA_ORDENES, "w", encoding="utf-8") as archivo:
            json.dump(datos, archivo, indent=4, ensure_ascii=False)

    def crear_orden(self, usuario_id, client_id, items, total, moneda, transaccion_id):
        """
        Crea y guarda una orden después de un pago exitoso.
        items: lista de dicts con { producto_id, nombre, cantidad, precio_unitario }
        """
        datos = self._leer_archivo()

        orden = {
            "id": str(uuid.uuid4())[:8].upper(),
            "usuario_id": usuario_id,
            "client_id": client_id,
            "items": items,
            "total": total,
            "moneda": moneda,
            "transaccion_id": transaccion_id,
            "estado": "PAGADA",
            "fecha": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }

        datos["ordenes"].append(orden)
        self._guardar_archivo(datos)

        return orden

    def obtener_ordenes_usuario(self, usuario_id):
        """Retorna todas las órdenes de un usuario final."""
        datos = self._leer_archivo()
        return [o for o in datos["ordenes"] if o["usuario_id"] == usuario_id]

    def obtener_ordenes_tienda(self, client_id):
        """Retorna todas las órdenes recibidas por una tienda."""
        datos = self._leer_archivo()
        return [o for o in datos["ordenes"] if o["client_id"] == client_id]
