from operacoes import ContaCorrente


opcao = 0

novaConta = ContaCorrente()


while opcao == 0:


    transacao = input('Por favor informe a opção desejada: 1- Saque | 2- Depósito: ')

    if transacao == '1':
        valorSaque = int(input('Informe o valor: '))
        print('Saldo Conta: ', novaConta.saque(valorSaque))

        opcao = int(input('Deseja realizar outra operação: 0- Sim | 1-Não: '))
        if opcao == 1:
            print('Obrigado por utilizar nossos serviços.')

    elif transacao == '2':
        valorDeposito = int(input('Informe o valor: '))
        print('Saldo Conta: ', novaConta.deposito(valorDeposito))
        opcao = int(input('Deseja realizar outra operação: 0- Sim | 1-Não: '))
        if opcao == 1:
            print('Obrigado por utilizar nossos serviços.')