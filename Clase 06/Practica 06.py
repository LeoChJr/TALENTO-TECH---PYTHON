nombres = ["Leonel","Ana","Luis","maria","","Jose","","Carlos","Marta",""]
for i in range(len(nombres)):
    if nombres[i] == "":
        print("Error: Nombre vacio")
        continue
    else:
        print(f"Nombre: {nombres[i].capitalize()} - Posicion: {i}")
        
