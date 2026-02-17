class Producto:
    def __init__(self, id, nombre, descripcion, precio, moneda, stock, categoria, client_id):
        self.id = id
        self.nombre = nombre
        self.descripcion = descripcion
        self.precio = precio
        self.moneda = moneda
        self.stock = stock
        self.categoria = categoria
        self.client_id = client_id

    def to_dict(self):
        return {
            "id": self.id,
            "nombre": self.nombre,
            "descripcion": self.descripcion,
            "precio": self.precio,
            "moneda": self.moneda,
            "stock": self.stock,
            "categoria": self.categoria,
            "client_id": self.client_id
        }
