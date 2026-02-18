from datetime import datetime

class CheckoutService:

    def __init__(self, cart_repository, order_repository):
        self.cart_repository = cart_repository
        self.order_repository = order_repository

    def checkout(self, user_id):

        cart = self.cart_repository.get_cart_by_user(user_id)

        # 1️ Validar carrito vacío
        if not cart or len(cart.get("products", [])) == 0:
            print("\nEl carrito está vacío. No se puede continuar.")
            return False

        print("\n========= RESUMEN DE COMPRA =========")

        total = 0
        for item in cart["products"]:
            subtotal = item["price"] * item["quantity"]
            total += subtotal
            print(f"{item['name']} x{item['quantity']} - ${subtotal}")

        print("-------------------------------------")
        print(f"TOTAL: ${total}")
        print("=====================================")

        # 2️ Confirmación
        confirmacion = input("\n¿Confirmar compra? (s/n): ")

        if confirmacion.lower() != "s":
            print("\nCompra cancelada.")
            return False

        # 3️ Crear orden
        order_data = {
            "user_id": user_id,
            "products": cart["products"],
            "total": total,
            "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }

        self.order_repository.save_order(order_data)

        # 4️ Vaciar carrito
        self.cart_repository.clear_cart(user_id)

        print("\nCompra realizada con éxito.")
        return True
    #fin checkout
