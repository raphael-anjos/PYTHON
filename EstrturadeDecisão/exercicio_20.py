nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
nota3 = float(input('Digite a terceira nota: '))

media = (nota1 + nota2 + nota3) / 3

if media == 10:
    print('Aprovado com destinção')
elif media >= 7:
    print('Aprovado, sua média foi: ', media)
elif media < 7:
    print('Reprovado, sua média foi: ', media)
else:
    print('O valor informado para as notas, não foi suficiente para calcular a média')