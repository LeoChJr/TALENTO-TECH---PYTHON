nombre_clientes = []
while True:
    print("Ingrese el nombre del cliente (o 'salir' para finalizar):")
    nombre = input("Nombre: ")
    if nombre.lower() == 'salir':
        break
    if nombre == "":
        print("Error: Nombre vacio")
        continue   
    nombre_clientes.append(nombre)
    
    
nombre_clientes.sort() #ordena la lista alfabeticamente
for i in range(len(nombre_clientes)):
    print(f"Cliente {i+1}: {nombre_clientes[i].capitalize()}")