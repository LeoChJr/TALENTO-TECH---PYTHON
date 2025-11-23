nombre = input("Ingrese su nombre:")
apellido = input("Ingrese su apellido:")
edad = input("Ingrese su edad:")
correo = input("Ingrese su correo electronico:")

if(nombre=="" or apellido=="" or edad=="" or correo=="" and edad>18):
    print("ERROR!")
else:
    print("Nombre:\t",nombre,"\nApellido:",apellido,"\nEdad:\t",edad,"\nCorreo:\t",correo)
    