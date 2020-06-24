ano = int(input('Informe o ano: '))

if ano % 2 == 0:
    print('{} é um ano bissexto'.format(ano))
else:
    print('{} não é um ano bissexto'.format(ano))