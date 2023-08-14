### importando blibilioteca para controlar tempo de exibição das mensagens (prints)
import time

# variavel para armazenar e apresentar opções do menu do sistema.

menu = '''

                    *** MENU - SISTEMA BANCÁRIO ***
   
                              OPÇÕES                              
     [s] Saque;                                                   
     [d] Depósito;                                                
     [e] Extrato;                                                 
     [q] Sair;                                                    
                                                                 
   
            
'''

# declarando variaveis e constantes
numero_depositos = 0
LIMITE_SAQUE = 3
saldo_conta = 0
saque_diario = 0

# listas que armazenam os depositos e saques realizados
depositos = []
saques = []

# loop infinito que vai ser executado até o usuário digitar a opção correspondente a sair
while True:
    print(menu)
    print("Digite a letra correspondente a opção que deseja executar\n")
    opcao = input("=> ")
    
    # deposito
    if opcao == "d":
        print(" *** DEPÓSITO ****")

        
        valor_deposito = float(input("Informe valor do depósito: "))
        if valor_deposito > 0:
                  saldo_conta += valor_deposito
                  depositos.append(valor_deposito)
                  print (f"Depósito realizado com sucesso, o valor R$ {valor_deposito:.2f} já está disponível na sua conta")
                  time.sleep(3)
                  print("Redirecionando usuário...")
        else:
            print("Valor inválido, tente novamente.")
            continue    

    # saque
    if opcao == "s":
        print(" *** SAQUE ****")

        if saque_diario < LIMITE_SAQUE:
                valor_saque = float(input("Informe valor do saque: "))
                # Loop que é executado até que usuário digite um valor menor ou igual a 500.
                if valor_saque > 0:
                    while valor_saque > 500:
                          print("O limite máximo para esta operação é R$ 500,00")
                          time.sleep(3)
                          print("Redirecionando usuário...")
                          valor_saque = float(input("Informe valor do saque dentro do limite: "))
                          if valor_saque <= 500:
                            continue # se verdadeiro exibe mensagem que a operação foi realizada com sucesso
                          else:
                            continue  # retorna para trecho onde é solicitado um valor menor ou igual 500.
            
                    if valor_saque > saldo_conta:
                        print("Saldo insuficiente !")
                        time.sleep(3)
                        print("Redirecionando usuário...")
                        continue
                    else:
                        print(f"Saque de R$ {valor_saque:.2f} realizado com sucesso, aguarde a contagem para retirar o valor.")
                        time.sleep(3)
                        saques.append(valor_saque)
                    saque_diario +=1 # variavel que recebe quantos saques foram realizados
                    saldo_conta -= valor_saque
                else:
                     print("Valor inválido, tente novamente.")    
                

        else:
            print("O limite diário para executar esta operação foi atingido, por favor tente novamente outro dia")
            time.sleep(5)
            print("Redirecionando usuário...")
            continue
                
    if opcao == "e":
            print(f'''
                  
                | ################################################################ |
                |                                                                  |
                |                  ***** EXTRATO BANCÁRIO ******                   |
                |                                                                  |
                |                                                                  |
                |                                                                  |
                | ################################################################ |
                \n''')
            for numero_depositos, valor_deposito in enumerate(depositos, start=1):
                print("\n***** DEPÓSITOS ******")
                print(f"Deposito {numero_depositos}, valor R$ {valor_deposito:.2f}")
        
            for saque_diario, valor_saque in enumerate(saques, start=1):
                print("\n***** SAQUES ******")
                print(f"Saque {saque_diario}, valor R${valor_saque:.2f}")

            print(f"\n***** SALDO DA CONTA ******")
            print(f"Saldo da conta R$ {saldo_conta:.2f}")
              
            time.sleep(10)
            print("Redirecionando usuário...")
    if opcao == "q":
        break    