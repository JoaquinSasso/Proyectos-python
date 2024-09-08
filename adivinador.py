import random
def adivinanza(x):
   num_aleatorio = random.randint(1,x)
   while num_elegido != num_aleatorio:
      num_elegido = int(input(f"Ingresa un numero entre 1 y {x}: "))
      if num_elegido > num_aleatorio:
         print("El numero secreto es menor")
      else:
         print("El numero secreto es mayor")    
   print("Adivinaste el numero! Felicitaciones!!!")
def adivina_PC(x):
   print("Ahora es el turno de adivinar de la computadora")
   bajo = 1
   alto = x
   respuesta = ''
   turnos = 0
   numero = random.randint(bajo, alto)
   while respuesta != 'C':
      turnos += 1
      respuesta = input(f'El numero que estas pensando es: {numero}?\nC: correcto\nP: es mas pequeño\nG: es mas grande\n')
      if respuesta == 'P':
         if(numero -1 < bajo):
            print("Eso es imposible, no puede ser mas pequeño")
            turnos -= 1
         else:
            alto = numero -1
            numero = random.randint(bajo, alto)
      elif respuesta == 'G':
         if(alto < numero + 1):
            print("Eso es imposible, no puede ser mas grande")
            turnos -= 1
         else:
            bajo = numero +1
            numero = random.randint(bajo, alto) 
   print(f"La computadora adivino correctamente el numero {numero} en {turnos} turnos")
adivina_PC(20)          