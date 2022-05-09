# # metodo matematico con factorial para saber si un numero es primo:
# Sí, el teorema de Wilson:
# Un número n es primo si y solo si (n-1)! + 1 es múltiplo de n
# Ejemplo:
# ¿Es 7 primo?
# 7 es primo si (7-1)! + 1 es múltiplo de 7
# (7-1)! + 1 = 6! + 1 = (6·5·4·3·2·1)+1 = 721
# ¿721 es múltiplo de 7?
# 721 : 7 = 103 (división exacta)
# 721 sí es múltiplo de 7 por tanto 7 es un número primo.
# #
def es_primo(numero):
    contador = 1
    for i in range(1, numero-1):
        contador *= (i+1)
    contador += 1
    if contador % numero == 0:
        return True
    else:
        return False


def run():
    numero = int(input("Ingrese un número:"))
    if es_primo(numero):
        print("Es primo")
    else:
        print("No es primo")


if __name__ == "__main__":
    run()
    print("""
    
    Este programa fue formulado con el teorema de Wilson...
    
            Este teorema formula la siguiente fórmula: 

                Un número n es primo si y solo si (n-1)! + 1 es múltiplo de n

    """)