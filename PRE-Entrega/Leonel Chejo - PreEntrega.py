productos = []

RESET = "\033[0m"     
AMARILLO = "\033[33m"
ANCHO = 80


opcion = ''

while opcion != '6':
    print("=" * ANCHO)
    print(f"{AMARILLO} {'crud - sistema de gestion basico'.upper().center(ANCHO)} {RESET}")
    print("=" * ANCHO)

    print("1. Agregar producto".ljust(25) + "2. Mostrar producto".ljust(25) + "3. Buscar producto".ljust(20))
    print("4. Actualizar producto".ljust(24) + " 5. Eliminar producto".ljust(25) + " 6. Salir".ljust(20))
    print("=" * ANCHO)

    opcion = input("Elige una opcion: ").strip()
    print("=" * ANCHO)
    
    match opcion:
        case "1":
            print(f"{AMARILLO} { 'Agregar PRODUCTOS'.upper().center(ANCHO) } {RESET}")
            print("-" * ANCHO)
            
            nombre_producto = input("Ingrese el nombre del producto: ").strip().title()
            while not nombre_producto.replace(" ", "").isalpha() or nombre_producto == "":
                nombre_producto = input("El nombre del producto esta vacio. Ingrese el nombre del producto: ").strip().title()
                
            categoria_producto = input("Ingrese la categoria del producto: ").strip().title()
            while not categoria_producto.replace(" ", "").isalpha() or categoria_producto == "":
                categoria_producto = input("La categoria del producto esta vacia. Ingrese la categoria del producto: ").strip().title()
                
            precio_producto = input("Ingrese el precio del producto: ").strip()
            while not precio_producto.replace('.', '', 1).isdigit() or precio_producto == "":
                precio_producto = input("El precio debe ser un numero. Ingrese el precio del producto: ").strip()
            
            productos.append([nombre_producto, categoria_producto, int(precio_producto)])
            print(f"{AMARILLO}Producto '{nombre_producto}' agregado {RESET}" )
               
        case "2":
            print(f"{AMARILLO} { " Ver PRODUCTOS".upper().center(ANCHO)} {RESET}")
            print("-" * ANCHO)
            
            if len(productos) == 0:
                print("No hay productos para mostrar".center(ANCHO))
            else:
                for i in range(len(productos)):
                    print(f"ID:[{i + 1}] - Nombre del producto: {productos[i][0]}, Categoria: {productos[i][1]}, Precio $: {productos[i][2]:.2f}")
                    print("-" * ANCHO)
        
        case "3":
            print(f"{AMARILLO} { 'buscar PRODUCTOS'.upper().center(ANCHO) } {RESET}")
            print("-" * ANCHO)
            
            if len(productos) == 0:
                print("No hay productos para buscar".center(ANCHO))
            else:
                busqueda_producto = input("Ingrese el nombre del producto a buscar: ").strip().title()
                encontrados = []
                for p in productos:
                    if busqueda_producto in p[0]:
                        encontrados.append(p)
                
                if len(encontrados) == 0:
                    print(f"No se encontraron productos con el nombre '{busqueda_producto}'.")
                else:
                    print(f"{len(encontrados)} producto(s) encontrado(s):")
                    for p in encontrados:
                        print(f"- Nombre: {p[0]}, Categoria: {p[1]}, Precio: ${p[2]}")
                        
                    
        case "4":
            print(f"{AMARILLO} { "actualizar PRODUCTOS".upper().center(ANCHO) } {RESET}")
            print("-" * ANCHO)
            
            if len(productos) == 0:
                print("No hay productos para actualizar".center(ANCHO))
            else:
                for i in range(len(productos)):
                    print(f"ID:[{i + 1}] - Nombre del producto: {productos[i][0]}, Categoria: {productos[i][1]}, Precio $: {productos[i][2]:.2f}")
                    print("-" * ANCHO)
                id = input("Ingrese el ID del producto que desea actualizar: ").strip()
                while not id.isdigit() or int(id) < 1 or int(id) > len(productos):
                    id = input("ID invalido. Ingrese el ID del producto que desea actualizar: ").strip()
                id = int(id) - 1
                
                nuevo_nombre_producto = input(f"Ingrese el nuevo nombre del producto (actual: {productos[id][0]}): ").strip().title()
                if nuevo_nombre_producto != "":
                    productos[id][0] = nuevo_nombre_producto
                
                nueva_categoria_producto = input(f"Ingrese el nuevo categoria del producto (actual: {productos[id][1]}): ").strip().title()
                if nueva_categoria_producto != "":
                    productos[id][1] = nueva_categoria_producto
                
                nuevo_precio = input(f"Ingrese el nuevo precio del producto (actual: {productos[id][2]:.2f}): ").strip()
                if nuevo_precio != "":
                    while not nuevo_precio.replace('.', '', 1).isdigit():
                         nuevo_precio = input("El precio debe ser un numero . Ingrese el nuevo precio del producto: ").strip()
                    productos[id][2] = float(nuevo_precio)
                
                print(f"{AMARILLO}Producto '{productos[id][0]}' actualizado {RESET}")
                
        case "5":
            print(f"{AMARILLO} { " eliminar PRODUCTOS".upper().center(ANCHO) } {RESET}")
            print("-" * ANCHO)
            
            if len(productos) == 0:
                print("No hay productos para eliminar.".center(ANCHO))
            else:
                for i in range(len(productos)):
                    print(f"ID:[{i + 1}] - Nombre del producto: {productos[i][0]}, Categoria: {productos[i][1]}, Precio: $ {productos[i][2]:.2f}")
                    print("-" * ANCHO)
                id = input("Ingrese el ID del producto que desea eliminar: ").strip()
                while not id.isdigit() or int(id) < 1 or int(id) > len(productos):
                    id = input("ID invalido. Ingrese el ID del producto que desea eliminar: ").strip()
                id = int(id) - 1
                
                eliminado = productos.pop(id)
                print(f"{AMARILLO}Producto '{eliminado[0]}' eliminado {RESET}")
                
        case "6":
            print(f"{AMARILLO} {" Gracias por usar nuestros sistemas!".upper().center(ANCHO) } {RESET}")
            print("-" * ANCHO)
        case _:
            print("❌ Opción inválida!".center(ANCHO))
            print("Opciones del 1 a 4 (5 para salir)".center(ANCHO))

    
