n=1
numero = float(input('Informe um numero: '))

if numero == round(numero):
    print('Inteiro')
else:
    print('Decimal')
    print('Arrendondado para baixo: ',round(numero-0.5))
    print('Arrendondado para cima: ', round(numero+0.5))