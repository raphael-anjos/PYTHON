valor_hora = int(input('Quanto você ganha por hora trabalhada? '))
hora_trabalho_mes = int(input('Quantas horas você trabalha por mês? '))
dias_trabalho_mes = int(input('Quantos dias trabalhou durante o mês? '))
hora_salario = valor_hora * hora_trabalho_mes
salario = hora_salario * dias_trabalho_mes

print('Seu salário em um mês é de:', salario)