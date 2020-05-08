precoL = 80
capacidadeL = 18

area = int(input('Informe a area total a ser pintada em m²: '))

litros = area / 3
quantidadeL = litros / capacidadeL
print('Você vai usar: ', quantidadeL,'lata(s) de tinta')
total = quantidadeL * precoL
print('Isso vai te custar: ', total)