
productos = {
    #nombres de productos : precios
    "manzana": 5000,
    "pera": 3000,
    "naranja": 4000
}

while True:
    nombre_del_producto = input("Ingrese el nombre del producto: (o 'salir' para terminar) ").strip().lower()
    
    if nombre_del_producto.lower() == 'salir':
        break   
    
    precio_del_producto = int(input("Ingrese el precio del producto: "))
    productos[nombre_del_producto] = precio_del_producto
    print("Producto agregado.")
    for producto, precio in productos.items():
        print(f"{producto.capitalize()}: ${precio}")    
    
print("Productos disponibles:")
for producto, precio in productos.items():
    print(f"{producto.capitalize()}: ${precio}")
# productos = {}

# while True:
#     nombre_del_producto = input("Ingrese el nombre del producto (o 'salir' para terminar): ").strip().lower()
#     if nombre_del_producto == 'salir':
#         break
#     precio_del_producto = input("Ingrese el precio del producto: ")
#     if not precio_del_producto.isdigit() or int(precio_del_producto) < 0:
#         print("El precio debe ser un número positivo.")
#         continue
#     productos[nombre_del_producto] = int(precio_del_producto)
#     print("Productos disponibles:")
#     for producto, precio in productos.items():
#         print(f"{producto.capitalize()}: ${precio}")

# print("\nListado final de productos:")
# for producto, precio in productos.items():
#     print(f"{producto.capitalize()}: ${precio}")