import json
import csv
import os

# CARGAR PRODUCTOS
def cargar_productos(archivo_productos):
    productos = []
    ids_registrados = set()
    categorias = set()

    try:
        with open(archivo_productos, "r", encoding="utf-8") as archivo:
            for linea in archivo:
                partes = linea.strip().split(",")
                
                # id, nombre, descripcion, precio, moneda, stock, categoria
                if len(partes) == 7:
                    producto = {
                        "id": partes[0],
                        "nombre": partes[1],
                        "descripcion": partes[2],
                        "precio": float(partes[3]),
                        "moneda": partes[4],
                        "stock": int(partes[5]),
                        "categoria": partes[6]
                    }
                    
                    productos.append(producto)
                    ids_registrados.add(partes[0])
                    categorias.add(partes[6])

    except FileNotFoundError:
        print("  Archivo de productos no encontrado. Se creará uno nuevo al guardar.")
    except ValueError:
        print("Error de formato en el archivo.")
    except Exception as e:
        print(f"Error inesperado: {e}")

    return productos, ids_registrados, categorias


