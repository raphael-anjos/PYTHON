altura = float(input('Informe sua altura em m: '))
sexo = input('Informe seu sexo: ')

if sexo == 'Masculino' or 'masculino':
    peso_ideal = (72.7 * altura) - 58
elif sexo == 'Feminino' or 'feminino':
    peso_ideal = (62.1 * altura) - 44.7


print('Seu peso ideal é:', peso_ideal,' KG')