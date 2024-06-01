from codebreaker import Code_Breaker

INTENTOS_TOTALES = 10
codebreaker = Code_Breaker()

intento = 0

print('Jugar Codebreaker!')

while intento <= INTENTOS_TOTALES:
   NUMBER = str(input('Numero:'))
   resolve = codebreaker.adivinar(NUMBER)
   intento += 1
   if resolve != "XXXX":
      print(resolve)
   else:
      print('You win!!')
      break
   

   
   
   

