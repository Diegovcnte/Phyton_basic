pesos = input("Ingrese la cantidad en pesos: ")
pesos = int(pesos)
dolar = 860
en_dolares = pesos / dolar
en_dolares = round(en_dolares, 2)
en_dolares = str(en_dolares)
pesos = str(pesos)
print(pesos+" pesos Chilenos es equivalente a "+en_dolares+" dolares Estado Unidenses.")