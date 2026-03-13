# Programa para adivinar un número

# librerias
import random

#-------
# input
#-------
print("-----------------------------")
print("---- Adivina el número ------")
print("-----------------------------")
print("La computadora ha generado un número entre 1 y 100....")
print("..... adivínalo.....")
computer_number= random.randint(1,100)
#-----------
# processing
#-----------
intento = -1
contador = 0

while intento != computer_number:
    intento=int(input("Adivine el numero que es del 1 hasta el 100: "))
    contador += 1

    if intento < computer_number:
        print("El numero es mas alto")
    elif intento > computer_number:
        print("El numero es mas bajo")



#-----------
# output
#-----------
print("FELICIDADES HAS ADIVINADO EL NUMERO")
print("Intentos realizados: ", contador)