from producto import *
from producto_db import *
from colorama import init,Fore

init(autoreset=True)

ANCHO = 100 #define el ancho 

def menu():
    print("=" * ANCHO)
    print(f"{Fore.GREEN + 'Gestion de Inventario'.upper().center(ANCHO)}") 
    print("=" * ANCHO)
    #muestra el menu con las opciones
    print("".ljust(10) + "1.➕ Agregar producto".ljust(25) + "2.📋 Mostrar producto".ljust(25) + "3.🔍 Buscar producto".ljust(20))
    print("".ljust(10) + "4.🔃 Actualizar producto".ljust(24) + " 5.❌ Eliminar producto".ljust(25) + "6. ⚠ Reporte bajo Stock".ljust(20))
    print("".ljust(10) + "7. Salir".ljust(20))
    print("=" * ANCHO)
    
def main(conexion):
    
    #crea la tabla de la base datos en caso de que no exista
    crear_tabla(conexion)
    
    #bucle infinito para mostrar el menu hasta que el usuario decida salir con la opcion 7
    while True:
        menu()
        opcion = input("Elige una opcion: ").strip()
        
        #dependiendo de la opcion elegida se llama a la funcion 
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
            #sale del programa mediante un break
            print(f"Saliendo del programa...")
            break
        else:
            print("Opcion invalida. Intenta de nuevo.")
    
    
#punto de entrada del programa
if __name__ == "__main__":
    conexion = conectar()
    if conexion:
        try:
            main(conexion)
        finally:
            cerrar_conexion(conexion)
            