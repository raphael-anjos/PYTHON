peso = float(input('Informe o peso dos peixes em kg: '))
excesso = peso - 50
multa = excesso * 4.00

print('Você excedeu', excesso,'kg alem do permitido')
print('O valor total da multa pelo execesso é de: ', multa,'R$')