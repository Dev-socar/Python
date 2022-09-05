"""2.Escribe un programa para un juego que consiste en adivinar una cadena de números distintos. 
Al principio, el programa debe pedir la longitud de la cadena (de 2 a 9 cifras). 
Después el programa debe ir pidiendo que intentes adivinar la cadena de números.
 En cada intento, el programa informará de cuántos números han sido acertados 
 (el programa considerará que se ha acertado un número si coincide el valor y la posición)."""

import random
import math
longitud = eval(input('Ingrese el número de dígitos que tendrá el número a adivinar: '))
coincidencias = 0
intentos = 1
while (longitud < 2) or (longitud > 9):   
        longitud = eval(input("Ingrese el número de dígitos en el siguiente rango [2-9]: "))

numeroList = random.sample(range(10), longitud)

digitsString = [str(integer) for integer in numeroList]
digitsString = "".join(digitsString)
numeroAdivinar = int(digitsString)


intento = eval(input('Ingrese su número propuesta: '))
intentoDigitos = int(math.log10(intento))+1

while intentoDigitos != longitud:
    intento = eval(input('Ingrese su número acorde al número de dígitos ingresado: '))
    intentoDigitos = int(math.log10(intento))+1


intentoList = [int(x) for x in str(intento)]
for i in range (0,longitud):
        print(intentoList[i], numeroList[i])
while intentoList != numeroList:
    intentos +=1
    for i in range (0,longitud):
        if intentoList[i] == numeroList[i]:
            coincidencias +=1
    print(f'tienes', coincidencias, 'coincidencias')
    intento = eval(input('Ingrese su número propuesta: '))
    intentoDigitos = int(math.log10(intento))+1
    while intentoDigitos != longitud:
        intento = eval(input('Ingrese su número acorde al número de dígitos ingresado: '))
        intentoDigitos = int(math.log10(intento))+1
    intentoList = [int(x) for x in str(intento)]

print ("Grandioso, adivinaste el número con solo ", intentos, "intentos.")