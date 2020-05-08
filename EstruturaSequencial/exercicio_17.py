precoL = 80
precoGl = 25

capacidadeL = 18
capacidadeGl = 3.6

area = int(input('Informe a area total a ser pintada em m²: '))

litros = area / 6
quantidadeL = litros / capacidadeL
print('Você vai precisar de: ', quantidadeL,'latas de tinta')
totalL = quantidadeL * precoL
print('Isso vai dar um total de RS:', totalL,'\n')

quantidadeGl = litros / capacidadeGl
print('Caso queira comprar galões, vai precisar de:', quantidadeGl,'galões de tinta')
totalGl = quantidadeGl * precoGl
print('Comprando galões o total fica em R$:', totalGl)