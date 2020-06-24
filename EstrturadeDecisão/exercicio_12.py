valorHora = float(input('Quanto você ganha por hora: '))
horaMes = float(input('Quantas horas trabalha durante o mês: '))

salarioBruto = valorHora * horaMes

if salarioBruto <= 900:
    descontoIR = 0.00
elif salarioBruto <= 1500:
    descontoIR = salarioBruto * 0.05
elif salarioBruto <= 2500:
    descontoIR = salarioBruto * 0.10
elif salarioBruto > 2500:
    descontoIR = salarioBruto * 0.20


descontoSind = salarioBruto * 0.03
descontoInss = salarioBruto * 0.10

fgts = salarioBruto * 0.11
totalDescontos = descontoInss + descontoIR + descontoSind

salarioLiquido = salarioBruto - descontoIR - descontoSind - descontoInss

print('Salário Bruto:', salarioBruto,'\n (-) IR:',descontoIR,'\n (-) INSS:', descontoInss,'\n (-) Sindicato:',descontoSind,
      '\n FGTS',fgts,'\n Total de descontos:', totalDescontos,'\n Salario Liquido:', salarioLiquido)