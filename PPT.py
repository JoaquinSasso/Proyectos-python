import random
def jugar():
   print("Estas por jugar a piedra papel o tijeras contra la computadora")
   jugada = int(input("Ingresa la jugada que deseas realizar\n1: Piedra\n2: Papel\n3: Tijeras\n"))
   jugada_pc = random.randint(1,3)
   if jugada_pc == jugada:
      print("Se produjo un empate")
   elif jugada_pc == 1: #Computadora elije piedra
      print("La computadora elijio piedra")
      if jugada == 2: #Jugador elije papel
         print("El jugador gana")
      if jugada == 3: #Jugador elije tijeras
         print("El jugador pierde")
   elif jugada_pc == 2: #Computadora elije papel
      print("La computadora elijio papel")
      if jugada == 1: #Jugador elije piedra
         print("El jugador pierde")
      if jugada == 3: #Jugador elije tijeras
         print("El jugador gana")
   elif jugada_pc == 3: #Computadora elije tijeras
      print("La computadora elijio tijeras")
      if jugada == 1: #Jugador elije piedra
         print("El jugador gana")
      if jugada == 2: #Jugador elije papel
         print("El jugador pierde")
jugar()