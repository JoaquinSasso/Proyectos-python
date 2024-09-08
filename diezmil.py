import random
import numpy #revisar el uso de funcion .replace para mejorar la funcion quitarDados
def quitarDados(numero, dados, dados_usados): #Esta funcion marca los dados que se utilizaron para descartarlos en la siguiente tirada
    for i in range(len(dados)):
        if dados[i] == numero:
            dados_usados[i] = 1
        if numero == 9: #Si se recime un 9 como numero quiere decir que todos los dados fueron utilizados a la vez (es el caso de la escalera)
            dados_usados[i] = 1
def tirarDados(dados, dados_usados):
    numeros_en_dados = [0,0,0,0,0,0]
    for i in range(len(dados)):
        if dados_usados[i] == 1:
            dados[i] = 9 #Los dados con un 9 son los que no se tiran
        else:
            dados[i] = random.randint(1,6)
            numeros_en_dados[dados[i] - 1] += 1
    print("Los dados que le tocaron son:")
    print(f"{dados}")
    return numeros_en_dados
def contarPuntos(numeros_en_dados, dados, dados_usados):
    puntuacion_acumulada = 0
    if numeros_en_dados[1] == 1 and numeros_en_dados[2] == 1 and numeros_en_dados[3] == 1 and numeros_en_dados[4] == 1 and (numeros_en_dados[0] == 1 or numeros_en_dados[5] == 1):
        puntuacion_acumulada += 2000
        quitarDados(9, dados, dados_usados)
    else:
        quitarDados(1, dados, dados_usados)
        quitarDados(5, dados, dados_usados)
        if numeros_en_dados[0] == 1: #Puntajes con los uno
            puntuacion_acumulada += 100
        if numeros_en_dados[0] == 2:
            puntuacion_acumulada += 200
        if numeros_en_dados[0] == 3:
            puntuacion_acumulada += 1000
        if numeros_en_dados[0] > 3:
            puntuacion_acumulada += 2000
        if numeros_en_dados[4] == 1: #Puntajes con los cinco
            puntuacion_acumulada += 50
        if numeros_en_dados[4] == 2:
            puntuacion_acumulada += 100    
        if numeros_en_dados[4] == 3:
            puntuacion_acumulada += 500
        if numeros_en_dados[4] > 3:
            puntuacion_acumulada += 2000
        if numeros_en_dados[1] == 3: #Puntajes con los dos
            puntuacion_acumulada += 200
            quitarDados(2, dados, dados_usados)
        if numeros_en_dados[1] > 3:
            puntuacion_acumulada += 2000
            quitarDados(2, dados, dados_usados)
        if numeros_en_dados[2] == 3: #Puntajes con los tres
            puntuacion_acumulada += 300
            quitarDados(3, dados, dados_usados) 
        if numeros_en_dados[2] > 3:
            puntuacion_acumulada += 2000
            quitarDados(3, dados, dados_usados)
        if numeros_en_dados[3] == 3: #Puntajes con los cuatro
            puntuacion_acumulada += 400 
            quitarDados(4, dados, dados_usados)
        if numeros_en_dados[3] > 3:
            puntuacion_acumulada += 2000
            quitarDados(4, dados, dados_usados)
        if numeros_en_dados[5] == 3: #Puntajes con los seis
            puntuacion_acumulada += 600 
            quitarDados(6, dados, dados_usados)
        if numeros_en_dados[5] > 3:
            puntuacion_acumulada += 2000
            quitarDados(6, dados, dados_usados)
    return puntuacion_acumulada
def gestionarTurno(puntuacion_acumulada, puntuaciones, se_uso_dados, i):
    if se_uso_dados:
                    if puntuacion_acumulada < 700 and puntuaciones[i] == 0:
                        print("No has alcanzado la puntuacion minima de 700, debes volver a tirar hasta llegar o perder")
                        input("Presione enter para seguir")
                        sigue_jugando = True  
                    else:
                        confirmacion = input("T para volver a tirar P para plantarse: ") 
                        while confirmacion != 'P' and confirmacion != 'T':
                            confirmacion = input("T para volver a tirar P para plantarse: ")
                        if confirmacion == 'T':
                            sigue_jugando = True
                        elif confirmacion == 'P':
                            sigue_jugando = False
                            if puntuaciones[i] == 0:
                                if puntuacion_acumulada > 700:
                                    puntuaciones[i] += puntuacion_acumulada
                            else:
                                puntuaciones[i] += puntuacion_acumulada
                                if puntuaciones[i] > 10000:
                                    aux = puntuaciones[i] - 10000
                                    puntuaciones[i] -= aux
                                    print(f"Te pasaste por {aux} puntos de los 10000")
    else: 
        sigue_jugando = False
        print("Ningún dado sirve. Has perdido la puntuacion acumulada")
        input("Presione enter para seguir")
    return sigue_jugando
def juego():
    nombres = [] #Array con los nombres de los jugadorse
    puntuaciones = [] #Array con las puntuaciones de los jugadores
    dados = [0,0,0,0,0] #Array con los dados
    victoria = False #Establece la condicion de victoria en falso para iniciar el juego
    cant_jugadores = int(input("Ingrese la cantidad de jugadores: "))
    for i in range(cant_jugadores):
        nombres.append(input(f"Ingrese el nombre del jugador {i+1}: "))
        puntuaciones.append(0)
    rondas = 0
    while victoria == False:
        rondas += 1
        for i in range(len(nombres)):
            print(f"\n\nEs el turno de: {nombres[i]}")
            puntuacion_acumulada = 0
            sigue_jugando = True
            dados_usados = [0,0,0,0,0]
            while(sigue_jugando == True):
                se_uso_dados = False
                if dados_usados == [1,1,1,1,1]: #Si ya se usaron todos los dados, todos vuelven a estar disponibles
                    dados_usados = [0,0,0,0,0]
                numeros_en_dados = tirarDados(dados, dados_usados)
                puntuacion_anterior = puntuacion_acumulada
                puntuacion_acumulada += contarPuntos(numeros_en_dados, dados, dados_usados)
                print(f"Se usaron los dados {dados_usados}")
                if puntuacion_anterior < puntuacion_acumulada:
                    se_uso_dados = True
                print(f"La puntuacion acumulada es de: {puntuacion_acumulada}")
                sigue_jugando = gestionarTurno(puntuacion_acumulada, puntuaciones, se_uso_dados, i)
                if puntuaciones[i] == 10000: #Comprobar si algun jugador gano la partida
                    print(f"{nombres[i]} ha ganado la partida")
                    victoria = True
                    break
            print(f"La puntuacion de {nombres[i]} es de: {puntuaciones[i]}")
    print(f"La partida ha finalizado en {rondas} rondas")
juego()