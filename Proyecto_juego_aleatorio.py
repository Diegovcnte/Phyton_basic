import random


def run():
    aleatorio = random.randint(1,100)
    bandera = True
    while bandera:
        eleccion = int(input("Seleccione un número entre 1 y 100: "))
        if eleccion == aleatorio:
            print("¡Has ganado el juego felicidades!")
            bandera = False
        elif eleccion < aleatorio:
            print("¡No te rindas! El número que buscas es mayor a tu elección")
            bandera = True
        elif eleccion > aleatorio:
            print("¡No te rindas! El número que buscas es menor a tu elección")
            bandera = True


if __name__ == "__main__":
    run()