numero1 = int(input('Informe um valor: '))
numero2 = int(input('Informe outro valor:'))

operacao = input('Escolha uma operação: 1-Soma | 2-Subtração | 3-Divisão | 4-Multiplicação: ')

if operacao == '1':
    resultado = numero1 + numero2
    print(resultado)
    if resultado % 2 == 0:
        print('Par')
    else:
        print('Ímpar')
    if resultado == round(resultado):
        print('Inteiro')
    else:
        print('Decimal')
    if resultado > 0:
        print('Positivo')
    else:
        print('Negativo')
elif operacao == '2':
    resultado = numero1 - numero2
    print(resultado)
    if resultado % 2 == 0:
        print('Par')
    else:
        print('Ímpar')
    if resultado == round(resultado):
        print('Inteiro')
    else:
        print('Decimal')
    if resultado > 0:
        print('Positivo')
    else:
        print('Negativo')
elif operacao == '3':
    resultado = numero1 / numero2
    print(resultado)
    if resultado % 2 == 0:
        print('Par')
    else:
        print('Ímpar')
    if resultado == round(resultado):
        print('Inteiro')
    else:
        print('Decimal')
    if resultado > 0:
        print('Positivo')
    else:
        print('Negativo')
elif operacao == '4':
    resultado = numero1 * numero2
    print(resultado)
    if resultado % 2 == 0:
        print('Par')
    else:
        print('Ímpar')
    if resultado == round(resultado):
        print('Inteiro')
    else:
        print('Decimal')
    if resultado > 0:
        print('Positivo')
    else:
        print('Negativo')