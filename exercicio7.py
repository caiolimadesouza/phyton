import math

numero = float(input('num: '))

if numero >= 0:
    raiz = math.sqrt(numero)
    print(f"raiz quadrade de {numero} é igual a {raiz}")
else:
    print("impossivel extrair raiz de numero negativo")