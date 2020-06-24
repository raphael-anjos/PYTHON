calcaJ = float(input('Qual o valor da calça Jeans: '))
calcaM = float(input('Qual o valor da calca de Moletom: '))
bermuda = float(input('Qual o valor da Bermuda: '))

if calcaJ < calcaM and calcaJ < bermuda:
    print('Você deve comprar uma calça Jeans')
elif calcaM < calcaJ and calcaM < bermuda:
    print('Você deve comprar uma calça de Moletom')
else:
    print('Você deve comprar uma Bermuda')
