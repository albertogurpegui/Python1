from pip._vendor.distlib.compat \
    import raw_input


def run():
    parar = 1
    while parar != 0:
        print("Introduzca un numero:")
        auxNumero = 0
        numero = int(raw_input())

        if numero == 0:
            parar = 0
        else:
            while numero != 0:
                auxNumero = auxNumero + numero
                numero = numero - 1
                parar = 0
            print(auxNumero)


run()
