# Programa para saber el numero de revotes de la pelota

# librerias
import math

#-------
# input
#-------

print("----------------------------------")
print("----------")
print("----------------------------------")


C1=int(input("DIGITA LA CAPITAL DE PEDRO: "))
C2=int(input("DIGITA LA CAPITAL DE JUAN: "))
C3=int(input("DIGITA LA CAPITAL NECESARIA PARA EL NEGOCIO: "))

#-----------
# processing
#-----------
MESES = 0

while (C1 + C2 < C3):
    C1 = C1+0.03*C1
    C2 = C2+0.03*C2
    MESES= MESES + 1

#-----------
# output
#-----------
print("-----------------------------------------")
print("PEDRO Y JUAN PUEDEN HACER EL NEGOCIO A LOS ",MESES, "meses")
print("-----------------------------------------")
