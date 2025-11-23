# #Diccionarios nos permiten almacenar datos en pares clave-valor
# #Se definen con llaves {}

# productos = {
#     "manzana": 5000,
#     "pera": 3000,
#     "naranja": 4000
# }

# precios_listas = [5000, 3000, 4000]

# print(precios_listas[0]) #Acceder al valor por indice
# print(productos["manzana"]) #Acceder al valor de una clave

# #Los diccionarios son mutables, se pueden agregar, modificar y eliminar elementos
# #Puede manejar varios tipos de datos como claves y valores

# #Algunos metodos utiles de los diccionarios
# print(productos.keys()) #Devuelve las claves del diccionario
# print(productos.values()) #Devuelve los valores del diccionario
# print(productos.items()) #Devuelve los pares clave-valor del diccionario    
# print(len(productos)) #Devuelve la cantidad de elementos en el diccionario
# print(productos.get("pera")) #Devuelve el valor de la clave especificada
# print(productos.pop("naranja")) #Elimina el elemento con la clave especificada y devuelve su valor
# print(productos.update({"kiwi": 6000})) #Agrega un nuevo par clave-valor al diccionario
# print(productos.clear())
# nuevo_producto = productos.copy() #Crea una copia del diccionario

# #----------------------------------------------------------------------
# cliente = {
#     #clave : valor
#     "nombre": "Lucia",
#     "edad" : 30,
#     "ciudad": "Bogota"
# }

# print(cliente.get("nombre")) #Acceder al valor de una clave
# print(cliente.get("Telefono")) #Acceder al valor de una clave

# print(cliente.keys()) #Devuelve las claves del diccionario

# print(cliente.values()) #Devuelve los valores del diccionario

# cliente.setdefault("Telefono", "123456789") #Agrega una nueva clave-valor si la clave no existe
# print(cliente.get("Telefono")) #Acceder al valor de una clave

# clientes = []

# while True:
#     print("Ingrese los datos del cliente (o 'salir' para finalizar):")
#     codigo = input("Codigo del cliente: ")
    
#     if codigo.lower() == 'salir':
#         break   
    
#     nombre = input("Nombre del cliente: ")
#     ciudad = input("Ciudad del cliente: ")
    
#     cliente = {
#         "codigo": codigo,
#         "nombre": nombre,
#         "ciudad": ciudad
#     }

#     clientes.append(cliente)

# print("\nLista de clientes:")
# for cliente in clientes:
#     print(f"Codigo: {cliente['codigo']}, Nombre: {cliente['nombre'].capitalize()}, Ciudad: {cliente['ciudad'].capitalize()}")   

# #----------------------------------------------------------------------

productos = {
    "manzana": 5000,
    "pera": 3000,
    "naranja": 4000
}

print("Productos disponibles:")
for producto, precio in productos.items():
    print(f"{producto.capitalize()}: ${precio}")    
    

while True:
    producto_buscado = input("Ingrese el nombre del producto a buscar (o 'salir' para finalizar): ")
    
    eliiminar_producto = input("Ingrese el nombre del producto a eliminar (o 'salir' para finalizar): ").lower()
    if eliiminar_producto.lower() == 'salir':
        break   
    
    if eliiminar_producto in productos:
        productos.pop(eliiminar_producto)
        print(f"Producto '{eliiminar_producto}' eliminado.")
    else:
        print(f"Producto '{eliiminar_producto}' no encontrado.")
        
        
    print("Productos disponibles:")
    for producto, precio in productos.items():
        print(f"{producto.capitalize()}: ${precio}")
        
print("Estado final de productos:")
for producto, precio in productos.items():
    print(f"{producto.capitalize()}: ${precio}")