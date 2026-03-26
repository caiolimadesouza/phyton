valor =float(input("valor da compra: "))
print("1 - dinheiro ou cheque, 10% de desconto")
print("2 - cartão de credito, 5% de descconto")
print("3 - 2x preço normal")
print("4 - 4x acrécimo de 7%")
forma_pgto = int(input("escolha uma das opções acima"))
match forma_pgto:
    case 1:
        desc = valor *0.1
        print (f'desconto foi de (desc), você pagara {valor - desc}')
    case 2:
        desc = valor * 0.05
        print(f"O desconto foi de (desc), você pagara {valor - desc}")
    case 3: 
        desc = valor /2
        print(f"O desconto foi de (desc), você pagara{valor - desc}")
    case 4:
        acrecimo = valor * 0.7
        parcela = (valor + acrecimo)
        print(f"o valor do produto será de{valor + acrecimo} em 4x {parcela}")
    case _:
        print("forma de pagamento invalida")