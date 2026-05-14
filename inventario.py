def registrar_producto(inventario, id_producto, nombre_producto, cantidad_producto):
    if id_producto in inventario:
        raise ValueError(f"El producto con ID {id_producto} ya existe en el inventario.")
    else:
        inventario[id_producto] = {
            "nombre": nombre_producto,
            "cantidad": cantidad_producto
        }
