# import Utilidades;

# Utilidades.saludar("Leonel")

# from Utilidades import saludar

# saludar("Leonel")

# import Utilidades as Util
# Util.saludar("Leonel")

# from Utilidades import *
# saludar("Leonel")


# import random

# def lanzar_dado():
#     dado1 = random.randint(1, 6)
#     dado2 = random.randint(1, 6)
#     suma = dado1 + dado2
    
#     return dado1, dado2, suma
# dado1, dado2, suma = lanzar_dado()
# print(f"Has lanzado un {dado1} y un {dado2}, sumando un total de {suma}.")


# import math

# radio = float(input("Ingrese el radio del circulo: "))
# area = math.pi * math.pow(radio, 2)
# print(f"El area del circulo con radio {radio} es: {area:.2f}")


# import datetime

# fecha_hora_actual = datetime.datetime.now()
# print("Fecha y hora actual:",fecha_hora_actual)
# print("Solo la fecha", fecha_hora_actual.strftime("%Y-%m-%d"))
# print("Solo la hora "   , fecha_hora_actual.strftime("%H:%M:%S"))

# print("Fecha legible:", fecha_hora_actual.strftime("%d de %B de %Y"))



from colorama import Fore, Back, init
 

init()
print(Back.GREEN + "HOla mundo")

print(Fore.BLUE +  Back.YELLOW + "Hola mundo ")

#para el proximo proyecto usar datatime y colorama