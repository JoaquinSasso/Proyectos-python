import timeit
import sys
sys.set_int_max_str_digits(300000)
def finobacci():
   num_objetivo = int(input("Ingrese la cantidad de numeros a generar: "))
   num_actual = 1
   num_anterior = 0
   num_previo = 0
   for i in range(num_objetivo):
      num_previo = num_anterior
      num_anterior = num_actual
      num_actual = num_anterior + num_previo
   print(f"{num_actual}")
print(timeit.timeit(finobacci, number=1))