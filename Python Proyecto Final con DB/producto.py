from producto_db import * #importa las funciones de producto_db.py
from colorama import Fore, Style #libreria para colores en la terminal

ANCHO = 100

#revisa que el valor ingresado sea un numero
def validar_numero(numero):
    while not numero.isdigit():
        numero = input("El valor debe ser un numero. Ingrese el valor: ").strip()
    return int(numero)

#revisa que el texto no este vacio o sea un numero
def validar_texto(texto):
    while texto == "" or texto.isdigit() :
        print("No puede estar vacio o ser un numero.")
        texto = input("Reingrese: ").strip()
    return texto

#funcion para agregar productos
def agregar_producto(conexion):
    print("-" * ANCHO)
    print(f"{Fore.YELLOW + 'Agregar PRODUCTOS'.upper().center(ANCHO)}")
    print("-" * ANCHO)
    nombre_producto = validar_texto(input("Ingrese el nombre del producto: ").strip().title())
    descripcion_producto = validar_texto(input("Ingrese la descripcion del producto: ").strip().title())
    cantidad_producto = validar_numero(input("Ingrese la cantidad del producto: "))
    precio_producto = validar_numero(input("Ingrese el precio del producto: "))
    categoria_producto = validar_texto(input("Ingrese la categoria del producto: ").strip().title())
    
    agregar_productos(conexion,nombre_producto, descripcion_producto, cantidad_producto, precio_producto, categoria_producto)
    print(Fore.CYAN + f"Producto '{nombre_producto}' agregado " )

#funcion para mostrar productos
def mostrar_producto(conexion):
    productos = mostrar_productos(conexion)
    if not productos:
        print("No hay productos para mostrar".center(ANCHO))
        return
    print("-" * ANCHO)
    print (Fore.YELLOW + "Lista de productos:".upper().center(ANCHO))
    print("-" * ANCHO)
    for producto in productos:
        print(f"ID: {producto[0]} - Nombre: {producto[1]} - Descripcion: {producto[2]} - Cantidad: {producto[3]} - Precio $:{producto[4]} - Categoria:{producto[5]}\n")

#funcion para buscar productos por id
def buscar_producto(conexion):
    print("-" * ANCHO)
    print(f"{Fore.YELLOW + 'buscar PRODUCTOS'.upper().center(ANCHO)}")
    print("-" * ANCHO)
    
    busqueda_producto = validar_numero(input("Ingrese el ID del producto a buscar: ").strip())
    encontrados = buscar_productos(conexion, busqueda_producto)
    
    if not encontrados:
        print(f"No se encontraron productos con el ID '{busqueda_producto}'")
    else:
        print("-" * ANCHO)
        print(Fore.YELLOW + f"{len(encontrados)} producto(s) encontrado(s) :".upper().center(ANCHO))
        print("-" * ANCHO)
        for p in encontrados:
            print(f"ID {p[0]} - Nombre: {p[1]}, Descripcion: {p[2]}, Cantidad: {p[3]}, Precio $: {p[4]} Categoria: {p[5]} \n")

#funcion para actualizar productos por id
def actualizar_producto(conexion):
    print("-" * ANCHO)
    mostrar_producto(conexion)
    print("-" * ANCHO)
    print(f"{Fore.YELLOW + 'Actualizar PRODUCTOS'.upper().center(ANCHO)}")
    print("-" * ANCHO)
    id_producto = validar_numero(input("Ingrese el ID del producto a actualizar: ").strip())
    nombre_producto = validar_texto(input("Ingrese el nuevo nombre del producto: ").strip().title())
    descripcion_producto = validar_texto(input("Ingrese la nueva descripcion del producto: ").strip().title())
    cantidad_producto = validar_numero((input("Ingrese la nueva cantidad del producto: ").strip()))
    precio_producto = validar_numero((input("Ingrese el nuevo precio del producto: ").strip()))
    categoria_producto = validar_texto(input("Ingrese la nueva categoria del producto: ").strip().title())  
    
    actualizar_productos(conexion,id_producto, nombre_producto, descripcion_producto, cantidad_producto, precio_producto, categoria_producto)
    print(Fore.CYAN + f"Producto con ID '{id_producto}' actualizado" )
   
#funcion para eliminar productos por id 
def eliminar_producto(conexion):
    print("-" * ANCHO)
    mostrar_producto(conexion)
    print("-" * ANCHO)
    print(f"{Fore.YELLOW + 'Eliminar PRODUCTOS'.upper().center(ANCHO)}")
    print("-" * ANCHO)
    id = validar_numero(input("Ingrese el ID del producto a eliminar: "))
    if eliminar_productos(conexion, id):
        print(Fore.CYAN + f"Producto ID '{id}' eliminado" )
    else:
        print(f"No se encontro ningun producto con ID '{id}'" )

#funcion para generar reporte de productos con bajo stocks
def reporte_bajo_stock(conexion):
    limite = validar_numero(input("Ingrese el limite de stock: "))
    productos_bajo_stock = reportes_bajo_stock(conexion, limite)
    
    if not productos_bajo_stock:
        print(f"No hay productos con stock menor a {limite}.")
        print("-" * ANCHO)
    else:
        print("-" * ANCHO)
        print(Fore.CYAN + f"Productos con stock menor a {limite}:".upper().center(ANCHO))
        print("-" * ANCHO)
        for producto in productos_bajo_stock:
            print(f"ID: {producto[0]} - Nombre: {producto[1]} - Cantidad: {producto[3]} \n")   