
nombre = input("Ingrese su nombre:")
apellido = input("Ingrese su apellido:")
edad = int(input("Ingrese su edad:"))
correo = input("Ingrese su correo electronico:").replace(" ","")

if correo.count("@")!=1:
    print("ERROR!")
else:
    if edad>=18:
        rango = "Mayor de edad"
    elif edad>15 and edad<18:
        rango="adolescente"
    elif edad <= 15:
        rango="niño"
    acumulado=0
    mes=1
    while mes<=6:
        ingresos = float(input("Ingrese sus ingresos mensuales: "))
        while ingresos < 0:
            print("Error: El ingreso no puede ser negativo.")
            ingresos = float(input("Ingrese sus ingresos mensuales: "))
        acumulado+=ingresos
        mes+=1
   
print("Nombre:\t",nombre,"\nApellido:",apellido,"\nEdad:\t",edad,"\nCorreo:\t",correo,"\nrango de edad:\t",rango,"\nIngresos en 6 meses:\t",acumulado)