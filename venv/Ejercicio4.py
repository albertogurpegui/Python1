
def bisiesto():

    parar = False
    while not parar:
        a = int(input("Ingresa año:\n"))
        if (a % 4 == 0 and a % 100 != 0 or a % 400 == 0):
            print("El año " + str(a) + " Si es bisiesto ")
        else:
            print("El año " + str(a) + " No es bisiesto ")


bisiesto()


