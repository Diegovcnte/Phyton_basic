def palindromo(palabra):
    palabra = palabra.replace(" ","").lower()
    if palabra[::] == palabra[::-1]:
        return True
    else:
        return False


def run():
    palabra = input("""
    Bienvenido al identificador de palíndromos
    ------------------------------------------
    Ingrese una palabra:
    """)
    if palindromo(palabra):
        print(palabra+" es palíndromo")
    else:
        print(palabra+" no es palíndromo")


if __name__ == "__main__":
    run()
