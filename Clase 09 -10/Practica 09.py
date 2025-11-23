productos = []


def agregar_producto():
    nombre_producto = input("Ingrese el nombre del producto: ").strip().title()
    
    productos.append(nombre_producto)
    print(f"Producto '{nombre_producto}' agregado.")

def consultar_productos():
    
    if productos:
        print("Lista de productos:")
        for i, producto in enumerate(productos, start=1):
            print(f"{i}. {producto}")
    else:   
        print("No hay productos para mostrar.")
    
    
def eliminar_producto():
    if productos:
        n_productos = input("Ingrese el numero de productos a eliminar: ").strip()
        if n_productos in productos:
            productos.remove(n_productos)
            print(f"Producto '{n_productos}' eliminado.")
        else:
            print(f"Producto '{n_productos}' no encontrado.")
    else:
        print("No hay productos para eliminar.")
                
    
def menu():
    print("1. Agregar producto")
    print("2. Consultar productos")
    
    
    print("5. Eliminar producto")
    print("6. Salir")
    opcion = input("Seleccione una opcion: ").strip()
    
    if opcion == "1":
        agregar_producto()
    elif opcion == "2":
        consultar_productos()
    elif opcion == "5":
        eliminar_producto()
    elif opcion == "6":
        print("Saliendo del programa...")
        return False
    else:
        print("Opcion no valida. Intente de nuevo.")
    return True


menu()

print("Hola")
