import uuid
import random
from datetime import datetime


class ServicioPago:

    def procesar_pago(self, numero_tarjeta, nombre_titular, mes_exp, anio_exp, cvv, monto, moneda):

        # Validar número de tarjeta (16 dígitos)
        numero_limpio = numero_tarjeta.replace(" ", "").replace("-", "")
        if not numero_limpio.isdigit() or len(numero_limpio) != 16:
            return False, "Número de tarjeta inválido. Debe tener 16 dígitos."

        # Validar titular
        if not nombre_titular.strip():
            return False, "El nombre del titular es obligatorio."

        # Validar fecha de expiración
        try:
            mes = int(mes_exp)
            anio = int(anio_exp)
            if mes < 1 or mes > 12:
                return False, "Mes de expiración inválido."
            ahora = datetime.now()
            if anio < ahora.year or (anio == ahora.year and mes < ahora.month):
                return False, "La tarjeta está vencida."
        except ValueError:
            return False, "Fecha de expiración inválida."

        # Validar CVV (3 o 4 dígitos)
        if not cvv.isdigit() or len(cvv) not in [3, 4]:
            return False, "CVV inválido."

        # Validar monto
        if monto <= 0:
            return False, "El monto debe ser mayor a cero."

        # Simulación: 90% de éxito, 10% de fallo aleatorio (fondos insuficientes)
        if random.random() < 0.1:
            return False, "Pago rechazado: fondos insuficientes (simulado)."

        # Generar ID de transacción
        transaccion_id = str(uuid.uuid4())[:12].upper()

        resultado = {
            "transaccion_id": transaccion_id,
            "monto": monto,
            "moneda": moneda,
            "fecha": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "tarjeta_terminada_en": numero_limpio[-4:],
            "estado": "APROBADO"
        }

        return True, resultado
