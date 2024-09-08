#include "stdio.h"
#include "time.h"
#include "stdlib.h"
/*piedra papel o tijeras
1 = Piedra
2 = Papel
3 = Tijeras*/
void jugar()
{
   int jugador, pc;
   printf("Ingresa la jugada que deseas realizar\n1: Piedra\n2: Papel\n3: Tijeras\n");
   scanf("%d", &jugador);
   pc = rand() % 3 + 1;
   if (pc == jugador)
   {
      printf("Ha ocurrido un empate\n");
   }
   else
   {
      switch (pc)
      {
      case 1:
         printf("La computadora eligio piedra\n");
         if (jugador == 2)
         {
            printf("El jugador gana\n");
         }
         else
         {
            printf("El jugador pierde\n");
         }
         break;
      case 2:
         printf("La computadora eligio papel\n");
         if (jugador == 3)
         {
            printf("El jugador gana\n");
         }
         else
         {
            printf("El jugador pierde\n");
         }
         break;
      case 3:
         printf("La computadora eligio tijera\n");
         if (jugador == 1)
         {
            printf("El jugador gana\n");
         }
         else
         {
            printf("El jugador pierde\n");
         }
         break;
      }
   }
}
int main()
{
   printf("Estas por jugar a piedra papel o tijeras contra la computadora\n");
   int repetir = 1;
   srand(time(NULL));
   while (repetir == 1)
   {
      jugar();
      printf("Ingresa 1 para volver a jugar, 0 para salir\n");
      scanf("%d", &repetir);
   }
   return 7;
}