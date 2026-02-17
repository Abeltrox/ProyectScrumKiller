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
                        "client_id": partes[7]  # ID de la tienda/cliente
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


# LISTAR PRODUCTOS DEL CLIENTE
def listar_mis_productos(productos, client_id):
    mis_productos = [p for p in productos if p['client_id'] == client_id]
    
    if not mis_productos:
        print("No tiene productos registrados en su tienda.")
        return

    print(f"\n{'ID':<10}{'Nombre':<20}{'Precio':<12}{'Stock':<8}{'Estado':<15}{'Categoría'}")
    print("-" * 90)

    for p in mis_productos:
        estado = "✅ Disponible" if p['stock'] > 0 else "❌ Agotado"
        print(
            f"{p['id']:<10}"
            f"{p['nombre']:<20}"
            f"{p['precio']} {p['moneda']:<8}"
            f"{p['stock']:<8}"
            f"{estado:<15}"
            f"{p['categoria']}"
        )


# BUSCAR PRODUCTO POR ID
def buscar_producto(productos, id_buscar):
    for p in productos:
        if p["id"] == id_buscar:
            return p
    return None


# CREAR PRODUCTO (CLIENTE LOGUEADO)
def crear_producto(productos, ids_registrados, client_id, nombre_tienda):
    """
    Permite al cliente logueado registrar productos en su tienda
    """
    print("\n" + "="*50)
    print(f"   REGISTRAR PRODUCTO EN '{nombre_tienda}'")
    print("="*50)
    
    # Generar ID automático
    if productos:
        ultimo_id = max([int(p["id"].replace("PROD", "")) for p in productos if p["id"].startswith("PROD")], default=0)
        id_p = f"PROD{ultimo_id + 1:04d}"
    else:
        id_p = "PROD0001"
    
    # Datos del producto
    nombre = input("Nombre del producto: ").strip()
    if not nombre:
        print(" El nombre es obligatorio.")
        return
    
    descripcion = input("Descripción: ").strip()
    
    try:
        precio = float(input("Precio: "))
        if precio < 0:
            print(" El precio no puede ser negativo.")
            return
    except ValueError:
        print(" Precio inválido.")
        return
    
    print("\nMoneda:")
    print("1. USD")
    print("2. EUR")
    print("3. COP")
    print("4. MXN")
    moneda_op = input("Seleccione (1/2/3/4): ").strip()
    
    if moneda_op == "1":
        moneda = "USD"
    elif moneda_op == "2":
        moneda = "EUR"
    elif moneda_op == "3":
        moneda = "COP"
    elif moneda_op == "4":
        moneda = "MXN"
    else:
        moneda = "USD"
    
    try:
        stock = int(input("Cantidad/Stock disponible: "))
        if stock < 0:
            print(" El stock no puede ser negativo.")
            return
    except ValueError:
        print(" Stock inválido.")
        return
    
    categoria = input("Categoría (ej: electrónica, ropa, hogar): ").strip()
    if not categoria:
        categoria = "general"

    producto = {
        "id": id_p,
        "nombre": nombre,
        "descripcion": descripcion,
        "precio": precio,
        "moneda": moneda,
        "stock": stock,
        "categoria": categoria,
        "client_id": client_id  # Se asocia a la tienda del cliente
    }

    productos.append(producto)
    ids_registrados.add(id_p)
    
    print("\n" + "="*50)
    print("     ✓ PRODUCTO CREADO EXITOSAMENTE")
    print("="*50)
    print(f"ID: {id_p}")
    print(f"Nombre: {nombre}")
    print(f"Precio: {precio} {moneda}")
    print(f"Stock: {stock}")
    print(f"Tienda: {nombre_tienda}")
    print("="*50)


# ACTUALIZAR PRODUCTO (SOLO SUS PROPIOS PRODUCTOS)
def actualizar_producto(productos, client_id):
    id_p = input("Ingrese el ID del producto a actualizar: ").strip()

    for p in productos:
        if p["id"] == id_p:
            # Verificar que el producto pertenece al cliente
            if p["client_id"] != client_id:
                print(" No tiene permisos para actualizar este producto.")
                return
            
            p["nombre"] = input(f"Nuevo nombre [{p['nombre']}]: ").strip() or p["nombre"]
            p["descripcion"] = input(f"Nueva descripción [{p['descripcion']}]: ").strip() or p["descripcion"]
            
            try:
                nuevo_precio = input(f"Nuevo precio [{p['precio']}]: ").strip()
                if nuevo_precio:
                    p["precio"] = float(nuevo_precio)
            except ValueError:
                print("Precio no modificado.")
            
            try:
                nuevo_stock = input(f"Nuevo stock [{p['stock']}]: ").strip()
                if nuevo_stock:
                    p["stock"] = int(nuevo_stock)
            except ValueError:
                print("Stock no modificado.")
            
            p["categoria"] = input(f"Nueva categoría [{p['categoria']}]: ").strip() or p["categoria"]

            print("✓ Producto actualizado correctamente.")
            return

    print(" Producto no encontrado.")


# ACTUALIZAR STOCK (SOLO SUS PROPIOS PRODUCTOS)
def actualizar_stock(productos, client_id):
    id_p = input("ID del producto: ").strip()
    
    for p in productos:
        if p["id"] == id_p:
            # Verificar que el producto pertenece al cliente
            if p["client_id"] != client_id:
                print(" No tiene permisos para actualizar este producto.")
                return
            
            try:
                nuevo_stock = int(input(f"Nuevo stock [{p['stock']}]: "))
                p["stock"] = nuevo_stock
                print("✓ Stock actualizado correctamente.")
                return
            except ValueError:
                print(" Stock inválido.")
                return
    
    print(" Producto no encontrado.")


# ELIMINAR PRODUCTO (SOLO SUS PROPIOS PRODUCTOS)
def eliminar_producto(productos, ids_registrados, client_id):
    id_p = input("Ingrese el ID del producto a eliminar: ").strip()

    for p in productos:
        if p["id"] == id_p:
            # Verificar que el producto pertenece al cliente
            if p["client_id"] != client_id:
                print(" No tiene permisos para eliminar este producto.")
                return
            
            confirmacion = input(f"¿Está seguro de eliminar '{p['nombre']}'? (s/n): ").lower().strip()
            if confirmacion == 's':
                productos.remove(p)
                ids_registrados.remove(id_p)
                print("✓ Producto eliminado correctamente.")
            else:
                print("Operación cancelada.")
            return

    print(" No se encontró un producto con ese ID.")


# GUARDAR PRODUCTOS
def guardar_productos(archivo_productos, productos):
    # Guardar en TXT
    try:
        with open(archivo_productos, "w", encoding="utf-8") as archivo:
            for p in productos:
                archivo.write(
                    f"{p['id']},{p['nombre']},{p['descripcion']},"
                    f"{p['precio']},{p['moneda']},{p['stock']},{p['categoria']},{p['client_id']}\n"
                )
        print("✓ Productos guardados en TXT.")
    except Exception as e:
        print(f" Error al guardar en TXT: {e}")

    # Guardar en JSON
    try:
        with open("productos.json", "w", encoding="utf-8") as archivo:
            json.dump(productos, archivo, indent=4, ensure_ascii=False)
        print("✓ Productos guardados en JSON.")
    except Exception as e:
        print(f" Error al guardar en JSON: {e}")

    # Guardar en CSV
    try:
        with open("productos.csv", "w", newline="", encoding="utf-8") as archivo:
            if productos:
                writer = csv.DictWriter(archivo, fieldnames=["id", "nombre", "descripcion", "precio", "moneda", "stock", "categoria", "client_id"])
                writer.writeheader()
                writer.writerows(productos)
        print("✓ Productos guardados en CSV.")
    except Exception as e:
        print(f" Error al guardar en CSV: {e}")


# MENÚ GESTOR DE PRODUCTOS (CLIENTE LOGUEADO)
def menu_gestor_productos(client_id, nombre_tienda):
    """
    Menú para que el cliente gestione los productos de su tienda
    Solo puede crear/editar/eliminar productos de su propia tienda
    """
    archivo = "productos.txt"
    productos, ids_registrados, categorias = cargar_productos(archivo)

    while True:
        print("\n" + "="*50)
        print(f"    GESTOR DE PRODUCTOS - {nombre_tienda}")
        print("="*50)
        print("1. Ver mis productos")
        print("2. Registrar nuevo producto")
        print("3. Buscar producto")
        print("4. Actualizar producto")
        print("5. Actualizar stock")
        print("6. Eliminar producto")
        print("7. Guardar cambios")
        print("8. Salir")
        print("="*50)

        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            listar_mis_productos(productos, client_id)

        elif opcion == "2":
            crear_producto(productos, ids_registrados, client_id, nombre_tienda)

        elif opcion == "3":
            id_buscar = input("Ingrese el ID del producto: ").strip()
            producto = buscar_producto(productos, id_buscar)
            if producto:
                if producto['client_id'] == client_id:
                    print("\n✓ Producto encontrado:")
                    print(f"ID: {producto['id']}")
                    print(f"Nombre: {producto['nombre']}")
                    print(f"Descripción: {producto['descripcion']}")
                    print(f"Precio: {producto['precio']} {producto['moneda']}")
                    print(f"Stock: {producto['stock']}")
                    print(f"Categoría: {producto['categoria']}")
                else:
                    print(" Este producto pertenece a otra tienda.")
            else:
                print(" Producto no encontrado.")

        elif opcion == "4":
            actualizar_producto(productos, client_id)

        elif opcion == "5":
            actualizar_stock(productos, client_id)

        elif opcion == "6":
            eliminar_producto(productos, ids_registrados, client_id)

        elif opcion == "7":
            guardar_productos(archivo, productos)

        elif opcion == "8":
            guardar = input("¿Desea guardar antes de salir? (s/n): ").lower().strip()
            if guardar == "s":
                guardar_productos(archivo, productos)
            print("Saliendo del gestor de productos...")
            break

        else:
            print(" Opción no válida. Intente nuevamente.")


if __name__ == "__main__":
    # Ejemplo de uso - simulando cliente logueado
    print("Simulando cliente logueado...")
    client_id = "CLI001"
    nombre_tienda = "Mi Tienda Demo"
    menu_gestor_productos(client_id, nombre_tienda)