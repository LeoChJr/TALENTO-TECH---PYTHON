from producto_db import *
RESET = "\033[0m"     
AMARILLO = "\033[33m"
ANCHO = 80

def validar_numero(numero):
    while not numero.isdigit():
        numero = input("El valor debe ser un numero. Ingrese el valor: ").strip()
    return int(numero)

def validar_texto(texto):
    while texto.strip() == "":
        print("No puede estar vacio ")
        texto = input("Reingrese: ").strip()
    return texto

def agregar_producto(conexion):
    print(f"{AMARILLO} { 'Agregar PRODUCTOS'.upper().center(ANCHO) } {RESET}")
    print("-" * ANCHO)
    nombre_producto = validar_texto(input("Ingrese el nombre del producto: ").strip().title())
    descripcion_producto = validar_texto(input("Ingrese la descripcion del producto: ").strip().title())
    cantidad_producto = validar_numero(input("Ingrese la cantidad del producto: "))
    precio_producto = validar_numero(input("Ingrese el precio del producto: "))
    categoria_producto = validar_texto(input("Ingrese la categoria del producto: ").strip().title())
    
    agregar_productos(conexion,nombre_producto, descripcion_producto, cantidad_producto, precio_producto, categoria_producto)
    print(f"{AMARILLO}Producto '{nombre_producto}' agregado {RESET}" )
    
    
def mostrar_producto(conexion):
    productos = mostrar_productos(conexion)
    if not productos:
        print("No hay productos para mostrar".center(ANCHO))
        return
    
    print ("Lista de productos:")
    for producto in productos:
            print(f"ID: {producto[0]}, Nombre: {producto[1]}, Descripcion: {producto[2]}, Cantidad: {producto[3]}, Precio:{producto[4]}, Categoria:{producto[5]}")

def buscar_producto(conexion):
    print(f"{AMARILLO} { 'buscar PRODUCTOS'.upper().center(ANCHO) } {RESET}")
    print("-" * ANCHO)
    
    busqueda_producto = validar_numero(input("Ingrese el ID del producto a buscar: ").strip())
    encontrados = buscar_productos(conexion, busqueda_producto)
    
    if not encontrados:
        print(f"No se encontraron productos con el id '{busqueda_producto}'.")
    else:
        print(f"{len(encontrados)} producto(s) encontrado(s) :")
        for p in encontrados:
            print(f"ID {p[0]} - Nombre: {p[1]}, Descripcion: {p[2]}, Cantidad: {p[3]}, Precio $: {p[4]} Categoria: {p[5]})")


def actualizar_producto(conexion):
    id_producto = validar_numero(input("Ingrese el ID del producto a actualizar: ").strip())
    nombre_producto = validar_texto(input("Ingrese el nuevo nombre del producto: ").strip().title())
    descripcion_producto = validar_texto(input("Ingrese la nueva descripcion del producto: ").strip().title())
    cantidad_producto = validar_numero((input("Ingrese la nueva cantidad del producto: ").strip()))
    precio_producto = validar_numero((input("Ingrese el nuevo precio del producto: ").strip()))
    categoria_producto = validar_texto(input("Ingrese la nueva categoria del producto: ").strip().title())  
    
    actualizar_productos(conexion,id_producto, nombre_producto, descripcion_producto, cantidad_producto, precio_producto, categoria_producto)
    print(f"{AMARILLO}Producto con ID '{id_producto}' actualizado con éxito. {RESET}" )
    
def eliminar_producto(conexion):
    id = validar_numero(input("Ingrese el ID del producto a eliminar: "))
    if eliminar_productos(conexion, id):
        print(f"{AMARILLO}Producto con ID '{id}' eliminado con éxito. {RESET}" )
    else:
        print(f"{AMARILLO}No se encontró ningún producto con ID '{id}'. {RESET}" )


def reporte_bajo_stock(conexion):
    umbral = validar_numero(input("Ingrese el umbral de stock: "))
    productos_bajo_stock = reportes_bajo_stock(conexion, umbral)
    
    if not productos_bajo_stock:
        print(f"No hay productos con stock menor a {umbral}.")
    else:
        print(f"Productos con stock menor a {umbral}:")
        for producto in productos_bajo_stock:
            print(f"ID: {producto[0]}, Nombre: {producto[1]}, Cantidad: {producto[3]}")   