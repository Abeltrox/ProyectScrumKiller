import uuid
from models.product import Producto
from repositories.product_repository import RepositorioProducto


class ServicioProducto:

    def __init__(self):
        self.repositorio = RepositorioProducto()

    # ==============================
    # ADMIN - Crear producto
    # ==============================
    def crear_producto(self, nombre, descripcion, precio, moneda, stock, categoria, client_id):

        if precio < 0:
            return False, "El precio no puede ser negativo."

        if stock < 0:
            return False, "El stock no puede ser negativo."

        producto_id = str(uuid.uuid4())[:8]

        producto = Producto(
            producto_id,
            nombre,
            descripcion,
            precio,
            moneda,
            stock,
            categoria,
            client_id
        )

        self.repositorio.guardar_producto(producto.to_dict())

        return True, "Producto creado correctamente."

    # ==============================
    # CATÁLOGO - Obtener productos de una tienda
    # ==============================
    def obtener_catalogo(self, client_id):
        return self.repositorio.obtener_por_tienda(client_id)

    # ==============================
    # Buscar producto por ID
    # ==============================
    def buscar_producto(self, producto_id):
        return self.repositorio.buscar_por_id(producto_id)
        # ==============================
    # ADMIN - Actualizar producto
    # ==============================
    def actualizar_producto(self, producto_id, datos_actualizados, client_id):

        producto = self.repositorio.buscar_por_id(producto_id)

        if not producto:
            return False, "Producto no encontrado."

        if producto["client_id"] != client_id:
            return False, "No tienes permiso para modificar este producto."

        # Actualizamos solo los campos enviados
        producto.update(datos_actualizados)

        exito = self.repositorio.actualizar_producto(producto)

        if exito:
            return True, "Producto actualizado correctamente."
        else:
            return False, "Error al actualizar el producto."

    # ==============================
    # ADMIN - Eliminar producto
    # ==============================
    def eliminar_producto(self, producto_id, client_id):

        producto = self.repositorio.buscar_por_id(producto_id)

        if not producto:
            return False, "Producto no encontrado."

        exito = self.repositorio.eliminar_producto(producto_id, client_id)

        if exito:
            return True, "Producto eliminado correctamente."
        else:
            return False, "No tienes permiso o el producto no existe."