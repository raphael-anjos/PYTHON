numero1 = int(input('Digite um numero: '))
numero2 = int(input('Digite outro numero: '))
numero3 = int(input('Digite mais um numero: '))

if numero1 > numero2 and numero1 > numero3:
    print(numero1)
elif numero2 > numero1 and numero2 > numero3:
    print(numero2)
else:
    print(numero3)
