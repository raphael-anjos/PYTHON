salario = float(input('Informe seu salario: '))
hora_trabalho = int(input('Informe as horas trabalhadas durante o mês: '))
dias_trabalho = int(input('Informe a quantidade de dias trabalhados no mês:'))

valor_hora = salario / dias_trabalho / hora_trabalho

print('Seu valor por hora trabalhada é:', valor_hora)