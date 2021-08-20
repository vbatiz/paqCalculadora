#testCalculadora.py --- Modulo principal para probar el paquete Calculadora 

# Importando modulos completos ---------------------------------------------

import os
import paqCalculadora.aditivo

# Importando objetos (funciones) individuales de un modulo -----------------

from paqCalculadora.multiplicativo import multiplicar
from paqCalculadora.multiplicativo import dividir

# Pudo ser tambien -------------------------------------------------------
# from paqCalculadora.multiplicativo import multiplicar, dividir


# Pausa -------------------------------------------------------------------

def pausa():
    print("Presiona <Enter> para continuar")
    input()

# Suma de dos numeros -----------------------------------------------------

def suma():
    os.system("clear")
    print("SUMA DE DOS NUMEROS")
    print("===================")
    a = float(input("A:"))
    b = float(input("B:"))

    c = paqCalculadora.aditivo.sumar(a,b)
    print("{0:5.2f} + {1:5.2f} = {2:5.2f}".format(a,b,c))
    pausa()

# Resta de dos numeros -----------------------------------------------------

def resta():
    os.system("clear")
    print("RESTA DE DOS NUMEROS")
    print("====================")
    a = float(input("A:"))
    b = float(input("B:"))

    c = paqCalculadora.aditivo.restar(a,b)
    print("{0:5.2f} - {1:5.2f} = {2:5.2f}".format(a,b,c))
    pausa()

# Multiplicacion dos numeros ------------------------------------------------

def multiplica():
    os.system("clear")
    print("MULTIPLICACION DE DOS NUMEROS")
    print("=============================")
    a = float(input("A:"))
    b = float(input("B:"))

    c = multiplicar(a,b)
    print("{0:5.2f} * {1:5.2f} = {2:5.2f}".format(a,b,c))
    pausa()

# División dos numeros ------------------------------------------------

def divide():
    os.system("clear")
    print("DIVISIÓN DE DOS NUMEROS")
    print("=======================")
    a = float(input("A:"))
    b = float(input("B:"))

    c = dividir(a,b)
    print("{0:5.2f} / {1:5.2f} = {2:5.2f}".format(a,b,c))
    pausa()

# Menu principal ----------------------------------------------------------

def menu():
    os.system("clear")
    print("CALCULADORA ARITMETICA")
    print("======================")
    print("1->Sumar")
    print("2->Restar")
    print("3->Multiplicar")
    print("4->Dividir")
    print("*->Salir")
    opcion = input("Opcion->")

    return opcion

if __name__ == "__main__":

    opcion = "1"
    while opcion != "*":
        opcion = menu()

        if opcion == "1":
            suma()
        elif opcion == "2":
            resta()
        elif opcion == "3":
            multiplica()
        elif opcion == "4":
            divide()
        
    os.system("clear")
    print("Fin de la calculadora...")