numA = float(input('digite um valor: '))
op = input('digite um desses operadores +-*/:')
numB = float(input('digite um valor: '))
if op == '+':
    resultado = numA + numB
if op == '-':
    resultado = numA - numB
if op == '*':
    resultado = numA * numB
if op== '/':
    resultado = numA / numB
print(f'{resultado}')