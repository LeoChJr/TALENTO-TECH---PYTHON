# productos = ["manzana", "banana", "cereza", "durazno", "pera"]

# for producto in productos:
#     print(producto)
#ejemplo con while
# productos = ["manzana", "banana", "cereza", "durazno", "pera"]
# i=0
# while i < len(productos):
#     print(productos[i])
#     i+=1

# palabra = "python"
# for letra in palabra:
#     print(f"Letra:{letra}")

#ejemplo del uso del break
# productos = ["manzana", "banana", "cereza", "durazno", "pera"]
# producto_buscado = "cereza"

# for producto in productos:
#     if producto == producto_buscado:
#         print(f"{producto} encontrado!")
#         break
#     print("Buscando...")

#Uso del range
#range(inicio, fin, paso)
# for i in range(5):
#     print(i)
# # Salida: 0, 1, 2, 3, 4
# for i in range(1, 6):
#     print(i)
    
# Salida: 1, 2, 3, 4, 5

# for i in range(1, 11, 2): #incremento
#     print(i)
# # Salida: 1, 3, 5, 7, 9

# for i in range(10, 0, -1):#decremento
#     print(i)
# # Salida: 10, 9, 8, 7, 6, 5, 4, 3, 2, 1

frutas = ["manzana", "banana", "cereza", "durazno", "pera"]
for i in range(len(frutas)):
    print(f"Fruta en indice {i} es {frutas[i]}")
    
