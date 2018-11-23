import re

def validatePassword():
    valida = False
    while not valida:
        password = input("Introduzca contraseña: ")
        if len(password) < 12:
            print("La contraseña elegida no tiene 12 caracteres")
        elif re.search('[0-9]',password) is None:
            print("La contraseña debe tener numeros")
        elif re.search('[A-Z]',password) is None:
            print("La contraseña debe tener alguna mayuscula")
        elif re.search('[a-z]',password) is None:
            print("La contraseña debe tener alguna minuscula")
        elif re.search('[! | " @ · # $ % & ¬ / ( ) = ? ¿ ¡ _ ^ * ` + { } < > , . ; :]',password) is None:
            print("La contraseña debe tener alguno caracter no alfanumerico")
        else:
            print("La contraseña elegida es segura")
            valida = True

validatePassword()