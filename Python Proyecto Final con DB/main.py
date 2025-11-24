from producto import *
from producto_db import *
from colorama import init,Fore

init(autoreset=True)

ANCHO = 100

def menu():
    print("=" * ANCHO)
    print(f"{Fore.GREEN + 'Gestion de Inventario'.upper().center(ANCHO)}") 
    print("=" * ANCHO)

    print("".ljust(10) + "1. Agregar producto".ljust(25) + "2. Mostrar producto".ljust(25) + "3. Buscar producto".ljust(20))
    print("".ljust(10) + "4. Actualizar producto".ljust(24) + " 5. Eliminar producto".ljust(25) + " 6. Reporte bajo Stock".ljust(20))
    print("".ljust(10) + "7. Salir".ljust(20))
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
            print(f"Saliendo del programa...")
            break
        else:
            print("Opcion invalida. Intenta de nuevo.")
    
    

if __name__ == "__main__":
    conexion = conectar()
    if conexion:
        try:
            main(conexion)
        finally:
            cerrar_conexion(conexion)
            