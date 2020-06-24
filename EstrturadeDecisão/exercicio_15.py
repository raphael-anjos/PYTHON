lado1 = int(input('Informe um valor: '))
lado2 = int(input('Informe outro valor: '))
lado3 = int(input('Informe mais um valor: '))

if lado1 + lado2 > lado3:
    print('Você formou um triangulo')
elif lado1 + lado3 > lado2:
    print('Você formou um triangulo')
elif lado2 + lado1 > lado3:
    print('Você formou um triangulo')
elif lado2 + lado3 > lado1:
    print('Você formou um triangulo')
elif lado3 + lado1 > lado2:
    print('Você formou um triangulo')
elif lado3 + lado2 > lado1:
    print('Você formou um triangulo')
else:
    print('Você não formou um triangulo')

