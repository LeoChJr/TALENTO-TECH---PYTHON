from producto import *
from producto_db import *
from colorama import Fore, Style

RESET = "\033[0m"     
AMARILLO = "\033[33m"
ANCHO = 80

def menu():
    print("=" * ANCHO)
    print(f"{AMARILLO} {'Gestion de Productos'.upper().center(ANCHO)} {RESET}")
    print("=" * ANCHO)

    print("1. Agregar producto".ljust(25) + "2. Mostrar producto".ljust(25) + "3. Buscar producto".ljust(20))
    print("4. Actualizar producto".ljust(24) + " 5. Eliminar producto".ljust(25) + " 6. Reporte bajo Stock".ljust(20))
    print("7. Salir".ljust(20))
    print("=" * ANCHO)
    
def main(conexion):
    crear_tabla(conexion)
    
    while True:
        menu()
        opcion = input("Elige una opcion: ").strip()
        
        if opcion == '1':
            
            agregar_producto(conexion)
            
        elif opcion == '2':
            mostrar_producto(conexion)
            
        elif opcion == '3':
            
            buscar_producto(conexion)
            
        elif opcion == '4':
            
            actualizar_producto(conexion)
            
        elif opcion == '5':
            
            eliminar_producto(conexion)
            
        elif opcion == '6':
            reporte_bajo_stock(conexion)
        elif opcion == '7':
            print(f"{AMARILLO}Saliendo del programa...{RESET}")
            break
        else:
            print("Opción inválida. Por favor, seleccione una opción válida.")
    
    

if __name__ == "__main__":
    conexion = conectar()
    if conexion:
        try:
            main(conexion)
        finally:
            cerrar_conexion(conexion)
            