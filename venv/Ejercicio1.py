import random
from pip._vendor.distlib.compat \
import raw_input

def funcionBuscar(numeroAleatorio):
    valor = False
    while not valor:
        print("Introduzca un numero:")
        print(numeroAleatorio)
        numero = int(raw_input())
        if numero == numeroAleatorio:
            print("Has acertado")
            valor = True
        elif numero > numeroAleatorio:
            print("El numero aleatorio es menor al escrito")
        else:
            print("El numero aleatorio es mayor que el escrito")


numeroAleatorio = random.randrange(1, 101)

funcionBuscar(numeroAleatorio)