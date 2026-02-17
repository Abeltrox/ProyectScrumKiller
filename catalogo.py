import json
import csv
import os

# CARGAR PRODUCTOS DESDE BASE DE DATOS
def cargar_productos_bd(archivo_productos):
    """
    Obtiene la información de productos desde la base de datos (archivo)
    Criterio: La información se obtiene desde la base de datos
    """
    productos = []

    try:
        with open(archivo_productos, "r", encoding="utf-8") as archivo:
            for linea in archivo:
                partes = linea.strip().split(",")
                
                # id, nombre, descripcion, precio, moneda, stock, categoria, client_id
                if len(partes) == 8:
                    producto = {
                        "id": partes[0],
                        "nombre": partes[1],
                        "descripcion": partes[2],
                        "precio": float(partes[3]),
                        "moneda": partes[4],
                        "stock": int(partes[5]),
                        "categoria": partes[6],
                        "client_id": partes[7]
                    }
                    
                    productos.append(producto)

    except FileNotFoundError:
        print("  No hay productos disponibles en la base de datos.")
    except ValueError as e:
        print(f"Error de formato en la base de datos: {e}")
    except Exception as e:
        print(f"Error al cargar productos: {e}")

    return productos


# CARGAR INFORMACIÓN DE TIENDAS/CLIENTES
def cargar_clientes_bd(archivo_clientes):
    """
    Obtiene información de las tiendas desde la base de datos
    """
    clientes = {}

    try:
        with open(archivo_clientes, "r", encoding="utf-8") as archivo:
            for linea in archivo:
                partes = linea.strip().split(",")
                
                # id, username, email, password, nombre_negocio, telefono, direccion
                if len(partes) == 7:
                    clientes[partes[0]] = {
                        "id": partes[0],
                        "nombre_negocio": partes[4]
                    }

    except FileNotFoundError:
        print("  No hay información de tiendas.")
    except Exception as e:
        print(f"Error al cargar tiendas: {e}")

    return clientes