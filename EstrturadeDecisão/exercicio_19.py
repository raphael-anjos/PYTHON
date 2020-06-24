numero = int(input('Informe um numero: '))

if numero < 1000:
    unidade = numero % 10
    numero = (numero - unidade) / 10

    dezena = numero % 10
    numero = (numero - dezena) / 10

    centena = numero

    dezena = int(dezena)
    centena = int(centena)

    print(centena, 'centena(s)', dezena, 'dezena(s)', unidade, 'unidade(s)')
else:
    print('Informe um numero inteiro menor que 1000')