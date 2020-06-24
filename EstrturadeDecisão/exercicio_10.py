turno = input('Qual turno você estuda: M-Matutino, V-Verpertino ou N-Noturno: ')


if turno == 'M' or turno == 'm':
    print('Bom dia !')
elif turno == 'V' or turno == 'v':
    print('Boa tarde !')
elif turno == 'N' or turno == 'n':
    print('Boa Noite !')
else:
    print('Opção inválida')