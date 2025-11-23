nombre = input("Ingrese su nombre:")
apellido = input("Ingrese su apellido:")
edad = int(input("Ingrese su edad:"))
correo = input("Ingrese su correo electronico:")

correo = correo.replace(" ","")
if correo.count("@")!=1:
    print("ERROR!")
else:
    if edad>=18:
        print("Mayor de edad")
    elif edad>15 and edad<18:
        print("adolescente")
    elif edad <= 15:
        print("niño")
    print("Nombre:\t",nombre.lower().title(),"\nApellido:",apellido.lower().title(),"\nEdad:\t",edad,"\nCorreo:\t",correo.strip().lower())

