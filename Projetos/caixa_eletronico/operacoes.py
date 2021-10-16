# Operações de Saque e Depósito em uma conta corrente
class ContaCorrente ():


    def __init__(self):
        self.saldoConta = 0
        self.contaAtiva = False



    def saque(self, valor):
        self.valorSaque = valor
        if self.contaAtiva == False: # Se a conta não estiver ativa, não permite realizar saque.
            print('Sua conta ainda não está ativa, realize um déposito para ativar')
        else:
            self.contaAtiva = True # Se a conta estiver ativa...
            if self.valorSaque > self.saldoConta: # verifica se existe saldo suficiente para realizar o saque.
                print('Erro ao efetuar saque, saldo insulficiente')
            else:
                print('Saque realizado com sucesso')
                self.saldoConta = self.saldoConta - self.valorSaque #subtrai o valor do saque do saldo da conta.
                # realiza a contagem de cédulas do valor solicitado no saque
                cem = int(valor / 100)
                valor = valor % 100
                cinquenta = int(valor / 50)
                valor = valor % 50
                dez = int(valor / 10)
                valor = valor % 10
                cinco = int(valor / 5)
                valor = valor % 5
                um = valor
                print(cem, 'Nota(s) de R$ 100')
                print(cinquenta, 'Nota(s) de R$ 50')
                print(dez, 'Nota(s) de R$ 10')
                print(cinco, 'Nota(s) de R$ 5')
                print(um, 'Nota(s) de R$ 1')
        return self.saldoConta

    def deposito(self, valor):
        self.valorDeposito = valor
        if valor < 10: #valor de depósito não pode ser superior a R$ 10,00
            print('O valor minimo para déposito é R$ 10,00')
            return self.saldoConta
        else:
            self.contaAtiva = True # Se valor do depósito for maior que R$ 10,00 ele ativa a conta, caso ainda esteja inativa
            print('Depósito realizado com sucesso')
            self.saldoConta = self.valorDeposito + self.saldoConta
        return self.saldoConta