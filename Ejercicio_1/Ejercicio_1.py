# Programa para validar el "Passwords"

# -----------------
# libraries
# -----------------

print("-------------------------------------------------------------------------")
print("------------EL PASSWORD ES CORRECTO O INCORRECTO--------")
print("-------------------------------------------------------------------------")
import math

# -----------------
# Intput
# -----------------

password= input("Digita la contraseña: ")
correct_password="python123"

# -----------------
# Procesing
# -----------------

while(password != correct_password):
    print("¡Error!: contraseña incorrecta")
    password=input("Digita de nuevo la contraseña: ")
    if(password == correct_password):
        print("ACCESO CONSEDIDO")

# -----------------
#outpt UwU
# -----------------

print("---------------------------------------------------------------------------")
print("---------------------------SI ERA TU CONTRASEÑA----------------------------")
print("---------------------------------------------------------------------------")