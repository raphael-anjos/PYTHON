nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))

media = (nota1 + nota2) / 2

if media >= 9.0:
    conceito = 'A'
elif media >= 7.5 and media < 9.0:
    conceito = 'B'
elif media >= 6.5 and media < 7.5:
    conceito = 'C'
elif media > 4.0 and media < 6.5:
    conceito = 'D'
elif media <= 4.0:
    conceito = 'E'


if conceito == 'A' or conceito == 'B' or conceito == 'C':
    print('Aprovado, sua média foi {}'.format(media),'com conceito {}'.format(conceito))
elif conceito == 'D' or conceito == 'E':
    print('Reprovado, sua média foi {}'.format(media), 'com ceito {}'.format(conceito))
