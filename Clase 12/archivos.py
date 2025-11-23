# archivo = open("datos.txt","w")
# # contenido = archivo.read()

# archivo.write("maria")

# archivo.write("ka")

# archivo.write("leo")


# archivo.close()

# archivo = open("datos.txt","r")
# print("Contenido del archivo")
# for linea in archivo:
#     print(linea.strip())
    
# archivo.close()



try:
    
    archivo = open("datos.txt","r")
    
    contenido = archivo.read()
    
    print(contenido)
    
    archivo.close()
except FileExistsError:
    print("Error")
