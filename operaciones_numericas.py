def run(menu, numero):
    print("Su elección ha sido "+str(menu)+" usted quiere conocer si el número "+numero+" es primo...")
    numero = int(numero)
    contador = 0
    for i in range(1, numero+1):
        if i == 1 or i == numero:
            continue
        if numero % i == 0:
            contador += 1
    if contador == 0:
        print("Es primo")
    else:
        print("No es primo")


def par_impar(menu, numero):
    print("Su elección ha sido "+str(menu)+" usted quiere conocer si el número "+numero+" es impar o par...")
    numero = int(numero)
    if numero % 2 == 0:
        print(str(numero)+" es par")
    else:
        print(str(numero)+" es impar")

def tablas(menu, numero):
    multiplo = input("Su elección ha sido "+str(menu)+" usted quiere conocer las tablas del "+str(numero)+" por favor digitalice la cantidad de tablas que desea conocer: ")
    numero = int(numero)
    multiplo = int(multiplo)
    for i in range(multiplo+1):
        print(str(numero)+" multiplicado por "+str(i)+" es equivalente a "+str(numero*i))
        




if __name__ == "__main__":
    numero = input("Ingrese un número: ")
    menu = input("""
    
    ¿Qué desea realizar con el número?
    1.- Conocer si es primo
    2.- Conocer si es par o impar
    3.- Conocer sus tablas de multiplicar

    Digite su elección: """)
    if menu == "1":
        run(1, numero)
    elif menu == "2":
        par_impar(2, numero)
    elif menu == "3":
        tablas(3, numero)
    else:
        print("seleccione una opción valida...")
