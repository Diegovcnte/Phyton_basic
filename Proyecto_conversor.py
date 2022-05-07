def conversor(eleccion, dolar):
    pesos = input("Ingrese la cantidad en pesos "+eleccion+": ")
    pesos = int(pesos)
    en_dolares = pesos / dolar
    en_dolares = round(en_dolares, 2)
    en_dolares = str(en_dolares)
    pesos = str(pesos)
    print(pesos+" pesos "+eleccion+" es equivalente a "+en_dolares+" dolares Estado Unidenses.")

menu = """
Bienvenido al conversor de monedas 💲

1.- Pesos Chilenos
2.- Pesos Argentinos
3.- Pesos Mexicanos
4.- Pesos Colombianos

----------------------------------------------------------------------------------------------------------------------
"""
print(menu)

residencia = int(input("Ingrese su preferencia: "))
if residencia == 1:
    conversor("Chilenos",860)
elif residencia == 2:
    conversor("Argentinos", 116.30)
elif residencia == 3:
    conversor("Mexicanos", 20.18)
elif residencia == 4:
    conversor("Colombianos",4049.50)
else:
    print("Elección no valida.")


