valor_hora = float(input('Quanto você ganha por hora trabalhada? '))
hora_trabalho_mes = int(input('Quantas horas você trabalha por dia? '))
dias_trabalho_mes = int(input('Quantos dias trabalhou durante o mês? '))

hora_salario = valor_hora * hora_trabalho_mes
#print(hora_salario)
salario_bruto = hora_salario * dias_trabalho_mes
#print(salario_bruto)

desconto_ir = salario_bruto * 0.11
#print(desconto_ir)
desconto_inss = salario_bruto * 0.08
#print(desconto_inss)
desconto_sindicato = salario_bruto * 0.05
#print(desconto_sindicato)

salario_liquido = salario_bruto - desconto_inss -desconto_ir - desconto_sindicato

print('Seu salário em um mês é de:', salario_liquido)