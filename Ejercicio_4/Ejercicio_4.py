# Programa para saber el numero de revotes de la pelota

# librerias
import math

#-------
# input
#-------

print("----------------------------------")
print("---- ¿cuantas veces reboto? ------")
print("----------------------------------")
print("......cuantos rebotes fueron......")
print("----------------------------------")

h=int(input("Digita la altura a la que vas a lanzar la pelota: " ))
q= h/5

#-----------
# processing
#-----------
contador = 0

while (h > q):
    contador += 1
    h= h*0.5
    if h < q:
        print("NUMERO DE VECES QUE REBOTO LA PELOTA ANTES DE PASAR LA LINEA DE LA QUINTA PARTE DE LA h: ", contador)
        






#-----------
# output
#-----------
print("-----------------------------------------")
print("FELICIDADES LA PELOTA REBOTO VARIAS VECES")
print("-----------------------------------------")

