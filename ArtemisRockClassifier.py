
print("Inicio del escáner de rocas Artemis Rover...\n")
basalt = 0
breccia = 0
highland = 0
regolith = 0
rockList = []

strPath = "rocks.txt"
fileObject = open(strPath)
line = fileObject.readline()
print(line)

rockList = fileObject.readlines()

for rock in rockList:
    print(rock)

fileObject.close()


def countMoonRocks(rockToID):
    global basalt
    global breccia
    global highland
    global regolith

    rockToID = rockToID.lower()

    if ("basalt" in rockToID):
        print("Encontre una roca de Basalto:")
        basalt += 1
    elif ("breccia" in rockToID):
        print("Encontre una roca de Brecha:")
        breccia += 1
    elif ("highland" in rockToID):
        print("Encontre una roca de Highland:")
        highland += 1
    elif ("regolith" in rockToID):
        print("Encontre una roca de Regolito:")
        regolith += 1

    return


for rock in rockList:
    countMoonRocks(rock)


def MaxRock(basalt, breccia, highland, regolith):
    if (basalt > breccia and basalt > highland and basalt > regolith):
        Rock_max = "Basaltos"
    elif (breccia > basalt and breccia > highland and basalt > regolith):
        Rock_max = "Brechas"
    elif (highland > basalt and highland > breccia and highland > regolith):
        Rock_max = "Highlands"
    else:
        Rock_max = "Regolitos"
    return Rock_max


def MinRock(basalt, breccia, highland, regolith):
    if (basalt < breccia and basalt < highland and basalt < regolith):
        Rock_Min = "Basaltos"
    elif (breccia < basalt and breccia < highland and breccia < regolith):
        Rock_Min = "Brechas"
    elif (highland < basalt and highland < breccia and highland < regolith):
        Rock_Min = "Highlands"
    else:
        Rock_Min = "Regolitos"
    return Rock_Min


Rock_max = MaxRock(basalt, breccia, highland, regolith)
Rock_min = MinRock(basalt, breccia, highland, regolith)
print("\n========== Recuento total de rocas ==========")
print("Numero de rocas e basalto es: ", basalt)
print("Numero de rocas de brecha es: ", breccia)
print("Numero de rocas de highland es: ", highland)
print("Numero de rocas de regolito es: ", regolith)

print("========== Numero maximo o minimo de rocas encontradas ==========")
print("El número máximo de un tipo de roca encontrado fue:",
      max(basalt, breccia, highland, regolith), Rock_max)
print("El número mínimo de un tipo de roca encontrado fue:",
      min(basalt, breccia, highland, regolith), Rock_min)
