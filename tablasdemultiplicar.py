def run(numero, limite):
    numero = int(numero)
    limite = int(limite)
    for i in range(limite+1):
        print(str(numero)+" por "+str(i)+" es equivalente a "+str(numero*i))


    


if __name__ == "__main__":
    numero = input("¿De qué número quiere obtener las tablas de múltiplicar?: ")
    limite = input("¿Hasta qué multiplo desea llegar?: ")
    run(numero, limite)
