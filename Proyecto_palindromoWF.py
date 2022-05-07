def palindromo(palabra):
    palabra = palabra.replace(" ","")
    palabra = palabra.lower()
    reverse = palabra[::-1]
    if palabra == reverse:
        return True
    else:
        return False


def run():
    palabra = input("""
    Bienvenido al identificador de palíndromos
    ------------------------------------------
    Ingrese una palabra:
    """)
    verificacion = palindromo(palabra)
    if verificacion == True:
        print(palabra+" es palíndromo")
    else:
        print(palabra+" no es palíndromo")


if __name__ == "__main__":
    run()
