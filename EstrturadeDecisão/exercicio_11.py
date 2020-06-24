salario = float(input('Informe seu salário: '))

if salario <= 280:
    reajuste = 20 / 100
    novoSalario = salario + (salario * reajuste)
    print('Seu salário era de:', salario)
    print('Seu reajuste foi de:', reajuste * 100, '%, que da um total de R$', salario * reajuste)
    print('Seu novo salario agora é:', novoSalario)
elif salario > 280 and salario < 700:
    reajuste = 15 / 100
    novoSalario = salario + (salario * reajuste)
    print('Seu salário era de:', salario)
    print('Seu reajuste foi de:', reajuste * 100, '%, que da um total de R$', salario * reajuste)
    print('Seu novo salario agora é:', novoSalario)
elif salario >= 700 and salario < 1500:
    reajuste = 10 / 100
    novoSalario = salario + (salario * reajuste)
    print('Seu salário era de:', salario)
    print('Seu reajuste foi de:', reajuste * 100, '%, que da um total de R$', salario * reajuste)
    print('Seu novo salario agora é:', novoSalario)
elif salario > 1500:
    reajuste = 5 / 100
    novoSalario = salario + (salario * reajuste)
    print('Seu salário era de:', salario)
    print('Seu reajuste foi de:', reajuste * 100, '%, que da um total de R$', salario * reajuste)
    print('Seu novo salario agora é:', novoSalario)