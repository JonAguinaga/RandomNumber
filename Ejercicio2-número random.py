import random

contador=5

print ("Introduce un número")

numero = int(input())

respuesta = random.randint(0 , 100)

while numero != respuesta and contador != 1:
    if numero == 42:
        print("Es la respuesta a todas las cosas menos a esta")
    if numero < respuesta - 20 or numero > respuesta + 20:
        print("Muy frío")
    elif numero < respuesta - 5:
        print("Un poco más")
    elif numero > respuesta + 5:
        print("Un poco menos")
    elif numero < respuesta:
        print("Un poquico más")
    elif numero > respuesta:
        print("Un poquico menos")
    elif contador == 0:
        print("Te has quedado sin vidas")
    contador = contador -1
    print("Prueba otra vez")
    print("Te quedan %i intentos" % contador)
    numero = int(input())

pass

if contador == 1:
    print("""Se te han acabado los intentos
Pulsa enter para salir""")

else:
    print("""yay!!
    Pulsa enter para vidas infinitas""")

input()
