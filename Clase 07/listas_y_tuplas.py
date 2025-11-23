# #Metodo append (permite agregar elementos al final de la lista)

# ventas = []

# print("Ingrese las ventas realizadas en el dia (ingrese -1 para finalizar):")

# while True:
#     monto = int(input("Monto de la venta: "))
#     if monto == -1:
#         break
#     ventas.append(monto)
    
# print("Ventas ingresadas")
# for venta in ventas:
#     print(f"-${venta}")

#Metodo remove (permite eliminar un elemento especifico de la lista)

# productos = ["manzana", "banana", "cereza", "durazno", "pera"]

# print("Listas de productos:")
# print(productos)

# print("Podes eliminar un producto de la lista - ingresa 'salir' para finalizar")

# while True:
#     producto_a_eliminar = input("Producto a eliminar: ").lower()
#     if producto_a_eliminar == "salir":
#         break
#     if producto_a_eliminar in productos:
#         productos.remove(producto_a_eliminar)
#         print(f"{producto_a_eliminar} eliminado.")
#     else:
#         print(f"{producto_a_eliminar} no encontrado en la lista.")
#     print("Productos actuales:", productos)

#pop sirve para eliminar un elemento en una posicion especifica
#insert sirve para insertar un elemento en una posicion especifica
#extend sirve para agregar multiples elementos a una lista
#index sirve para obtener la posicion de un elemento en la lista
#count sirve para contar cuantas veces aparece un elemento en la lista
#sort sirve para ordenar los elementos de una lista
#reverse sirve para invertir el orden de los elementos en una lista
#len sirve para obtener la cantidad de elementos en una lista
#clean sirve para limpiar todos los elementos de una lista


# las listas son mejores para almacenar datos que pueden cambiar, mientras que las tuplas son mejores para datos que no deben cambiar.
#--------------------------------------------------------------------------

#Tuplas son inmutables (no se pueden modificar una vez creadas) y usan parentesis ()

numeros = (1,2,3,4,5,3,3,3)
print(numeros.count(3)) #cuenta cuantas veces aparece el elemento 3 en la tupla 

#tambien se puede usar el index

#Se puede convertir listas en tuplas y viceversa

mi_listas = [10,20,30,40]
mi_tupla = tuple(mi_listas)
print(mi_tupla)

otra_tupla = (50,60,70,80)
otra_lista = list(otra_tupla)
print(otra_lista)

#--------------------------------------------------------------------------
#Slices en lsitas y tuplas
#Sintaxis de slices: lista[inicio:fin:paso]

numeros = [0,1,2,3,4,5,6,7,8,9]

print(numeros[:3]) #Salida: [0, 1, 2]
print(numeros[3:]) #Salida: [3, 4, 5, 6, 7, 8, 9]
print(numeros[2:7]) #Salida: [2, 3, 4, 5, 6]
print(numeros[1:8:2]) #Salida: [1, 3, 5, 7]

#Con las tuplas es similar



