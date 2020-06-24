saque = int(input('Informe o valor que deseja sacar: '))

if saque < 10 and saque > 600:
    print('O valor minimo para saque é: R$ 10 e o valor máximo é R$ 600')
else:
    print('Valor solicitado R$: ', saque)
cem = int(saque / 100)
saque = saque % 100

cinquenta = int(saque / 50)
saque = saque % 50

dez = int(saque / 10)
saque = saque % 10

cinco = int(saque / 5)
saque = saque % 5

um = saque

print(cem, 'Nota(s) de R$ 100')
print(cinquenta,'Nota(s) de R$ 50')
print(dez, 'Nota(s) de R$ 10')
print(cinco, 'Nota(s) de R$ 5')
print(um, 'Nota(s) de R$ 1')