# Josmar Gustavo Palomino Castelan
# Josmar360

# Imprime un mensaje de inicio.
print("Inicio del escáner de rocas Artemis Rover...\n")

# Inicializa contadores para cada tipo de roca.
basalt = 0
breccia = 0
highland = 0
regolith = 0

# Crea una lista vacía para almacenar información sobre las rocas.
rockList = []

# Ruta del archivo que contiene información sobre las rocas.
strPath = "rocks.txt"

# Abre el archivo en modo lectura.
fileObject = open(strPath)

# Lee la primera línea del archivo y la imprime.
line = fileObject.readline()
print(line)

# Lee todas las líneas restantes del archivo y las almacena en rockList.
rockList = fileObject.readlines()

# Cierra el archivo.
fileObject.close()

# Define una función para contar el número de rocas de diferentes tipos.
def countMoonRocks(rockToID):
    global basalt, breccia, highland, regolith

    # Convierte el nombre de la roca a minúsculas para facilitar la comparación.
    rockToID = rockToID.lower()

    # Compara el tipo de roca y actualiza el contador correspondiente.
    if "basalt" in rockToID:
        print("Encontre una roca de Basalto:")
        basalt += 1
    elif "breccia" in rockToID:
        print("Encontre una roca de Brecha:")
        breccia += 1
    elif "highland" in rockToID:
        print("Encontre una roca de Highland:")
        highland += 1
    elif "regolith" in rockToID:
        print("Encontre una roca de Regolito:")
        regolith += 1

    return

# Llama a la función countMoonRocks para cada roca en rockList.
for rock in rockList:
    countMoonRocks(rock)

# Define una función para determinar el tipo de roca con el recuento máximo y mínimo.
def MaxRock(basalt, breccia, highland, regolith):
    if basalt > breccia and basalt > highland and basalt > regolith:
        Rock_max = "Basaltos"
    elif breccia > basalt and breccia > highland and breccia > regolith:
        Rock_max = "Brechas"
    elif highland > basalt and highland > breccia and highland > regolith:
        Rock_max = "Highlands"
    else:
        Rock_max = "Regolitos"
    return Rock_max

# Define una función para determinar el tipo de roca con el recuento mínimo.
def MinRock(basalt, breccia, highland, regolith):
    if basalt < breccia and basalt < highland and basalt < regolith:
        Rock_Min = "Basaltos"
    elif breccia < basalt and breccia < highland and breccia < regolith:
        Rock_Min = "Brechas"
    elif highland < basalt and highland < breccia and highland < regolith:
        Rock_Min = "Highlands"
    else:
        Rock_Min = "Regolitos"
    return Rock_Min

# Llama a las funciones MaxRock y MinRock para determinar el tipo de roca con el recuento máximo y mínimo.
Rock_max = MaxRock(basalt, breccia, highland, regolith)
Rock_min = MinRock(basalt, breccia, highland, regolith)

# Imprime estadísticas sobre las rocas encontradas.
print("\n========== Recuento total de rocas ==========")
print("Numero de rocas de basalto es: ", basalt)
print("Numero de rocas de brecha es: ", breccia)
print("Numero de rocas de highland es: ", highland)
print("Numero de rocas de regolito es: ", regolith)

print("========== Numero máximo o mínimo de rocas encontradas ==========")
print("El número máximo de un tipo de roca encontrado fue:",
      max(basalt, breccia, highland, regolith), Rock_max)
print("El número mínimo de un tipo de roca encontrado fue:",
      min(basalt, breccia, highland, regolith), Rock_min)
