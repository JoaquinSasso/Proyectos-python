#input = [1,1,2,3,5,8,13,21,34,55,89,144,233,377]
input = [233,377]
#input = [1,1,2,3,5,8,13,21,34]
i = 1
continuar = True
posible = True
if len(input) < 3:
   print("No se puede analizar si la cadena es una secuencia de Finobacci debido a que no tiene al menos 3 elementos")
   posible = False
while i < (len(input)-1) and continuar == True and posible == True:
   i += 1
   if input[i] == input[i-2] + input[i-1]:
      continuar = True
   else:
      continuar = False
if posible == True and continuar == True:
   print("La cadena era una secuencia de Finobacci")
if posible == True and continuar == False:
   print(f"La cadena no era una secuencia de Finobacci porque {input[i]} no es el resultado de {input[i-2]} + {input[i-1]}")