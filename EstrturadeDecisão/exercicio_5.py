nota1 = int(input('Digite a primeira Nota: '))
nota2 = int(input('Digite a segunda nota: '))

media = (nota1 + nota2) / 2

if media >= 7:
    if media == 10:
        print('Aprovado com distinção')
    else:
        print('Aprovado')
else:
    print('Reprovado')
