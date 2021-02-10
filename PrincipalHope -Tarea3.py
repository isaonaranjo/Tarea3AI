####################################
# Maria Isabel Ortiz Naranjo
# 18176
# 9 de febrero de 2021
####################################

# funcion mostrarMatriz
def mostrarMatriz(matriz):
    print ("   0  1  2  3  4  5  6  7  8  9")
    for x in range(10):
        print (x, matriz[x])

# funcion valida movimiento step
def validaStep(filai, coli, filaf, colf):
    bandera = False
    if (filaf-1) == filai or (filaf+1) == filai:
        if colf >= (coli-1) and colf <= (coli+1):
            bandera = True
    if (filaf == filai):
        if (coli-1) == colf or (coli+1) == colf:
            bandera = True
    return bandera

# funcion valida movimiento hope
def validaHope(filai, coli, filaf, colf):
    bandera = False
    if (filaf-2) == filai or (filaf+2) == filai or (filaf == filai):
        if colf == (coli-2) or colf == (coli+2):
            bandera = True
    return bandera

# funcion movimiento step
def step(filai, coli, filaf, colf, jugador):
    if validaStep(filai, coli, filaf, colf) == True:
        if matriz[filaf][colf] == 0:
            matriz[filaf][colf] = jugador
            matriz[filai][coli] = 0
        else:
            print ("La posicion final esta ocupada")
    else:
        print ("Movimiento invalido")

# funcion movimiento hope
def hope(filai, coli, filaf, colf, jugador):
    if validaHope(filai, coli, filaf, colf) == True:
        if matriz[filaf][colf]== 0:
            matriz[filaf][colf] = jugador
            matriz[filai][coli] = 0
        else:
            print ("La posicion final esta ocupada")
    else:
        print ("Movimiento invalido")

# Funcion cambiar jugador
def cambiarJugador(jugador):
    if jugador == 1:
        jugador = 2
    else:
        jugador = 1
    return jugador

# Funcion gana: cuando todas las fichas de un jugador estan en la posicion del otro jugador
def gana(jugador):
    cantidad1 = 0
    cantidad2 = 0
    #verifica si el jugador 1 llego a la esquina del jugador 2
    if jugador == 1:
        veces = 6
        fila = 9
        contfila = 0
        filas = 5
        while contfila < filas:
            veces = veces-1
            col = 9
            cont = 0
            while cont < veces:
                #print ("Col: ", col, "Cant1: ", cantidad1)
                if matriz[fila][col] == jugador: #jugador
                    cantidad1 = cantidad1 + 1
                cont = cont + 1
                col = col - 1
            fila = fila-1
            contfila = contfila+1
    if cantidad1 == 15: #gana el jugador 1
        return 1

    #verifica si el jugador 2 llego a la esquina del jugador 1
    if jugador == 2:
        veces = 6
        fila = 0
        contfila = 0
        filas = 5
        while contfila < filas:
            veces = veces-1
            col = 0
            cont = 0
            while cont < veces:
                #print ("Col: ", col, "Cant2: ", cantidad2)
                if matriz[fila][col] == jugador: #jugador
                    cantidad2 = cantidad2 + 1
                cont = cont + 1
                col = col + 1
            fila = fila+1
            contfila = contfila+1
    if cantidad2 == 15: #gana el jugador 2
        return 2

    return 0 #no hay ganador
    
    
    
####################################
# Principal
####################################
# Inicializar variables
ganar = False
jugador = 1
# Definir matriz
matriz = [[1,1,1,1,1,0,0,0,0,0],
          [1,1,1,1,0,0,0,0,0,0],
          [1,1,1,0,0,0,0,0,0,0],
          [1,1,0,0,0,0,0,0,0,0],
          [1,0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0,2],
          [0,0,0,0,0,0,0,0,2,2],
          [0,0,0,0,0,0,0,2,2,2],
          [0,0,0,0,0,0,2,2,2,2],
          [0,0,0,0,0,2,2,2,2,2]]

mostrarMatriz(matriz)
    
while (ganar == False):
    #Ingresar datos del movimiento: coordenada inicial y final
    print ("***Jugador***: ", jugador)
    filai = int (input("Fila inicial (0-9): "))
    coli = int (input("Columna inicial (0-9): "))
    filaf = int (input("Fila final (0-9): "))
    colf = int (input("Columna final (0-9): "))
    opcion = input("¿step(s) o hope(h)?")
    #Step
    if opcion == "s":
        step(filai, coli, filaf, colf, jugador)
        mostrarMatriz(matriz)
        resultado = gana(jugador)
        if resultado == 1 or resultado == 2:
            ganar = True;
            print ("El jugador ", jugador, " ha ganado")
        else:
            jugador = cambiarJugador(jugador)
    #Hope
    if opcion == "h":
        hope(filai, coli, filaf, colf, jugador)
        mostrarMatriz(matriz)
        resultado = gana(jugador)
        if resultado == 1 or resultado == 2:
            ganar = True;
            print ("El jugador ", jugador, " ha ganado")
        else:
            jugador = cambiarJugador(jugador)

print ("fin del juego")
            
        
