import random
import math

menor_valor = int(input("Informe um número de menor valor: ")) # usuario informa um valor incial
maior_valor = int(input("Informe um número de maior valor: ")) # usuário informa um valor final

x = random.randint(menor_valor,maior_valor) # através da função randon, um número aleatório (de acordo com que foi informado em menor_valor e maior_valor) é salvo na variável x
print("\n\t Você tem ", round(math.log(maior_valor - menor_valor + 1,2)),"chances de adivinhar o número!\n") # de acordo com os valores informado pelo usuário é gerado um número de tentativas para adivinhar o número

count = 0 # definimos um contatod com valor inicial 0

while count < math.log(maior_valor - menor_valor + 1,2): # enquanto o valor do contador for menor que número de tentativas
    count+=1 # incrementa 1 ao no variável count

    adivinhe = int(input("Adivinhe o número: ")) # usuário entra com um número para tentar adivinhar qual o número salvo na variável x

    if x == adivinhe: # se o número informado pelo usuário for igual ao que foi armazenado na variavem x
        print("Parabéns você conseguiu adivinhar em", count,"tentativas") # uma mensagem é retornada com número de tentativas ele conseguiu adivinhar
        break # encerramos o a estrutura if, pois a condição já foi satisfeita
    elif x > adivinhe: # se o valor da variável x for um número muito grande do número informado pelo usuário
        print("Tente novamente !""\nSeu palpite:" ,adivinhe,"muito pequeno") # retornamos uma mensagem que o palpite do usuário é número muito pequeno
    elif x < adivinhe: # se o valor da variável x for um número muito pequeno do número informado pelo usuário
        print("Tente novamente !""\nSeu palpite:" ,adivinhe,"muito grande")  # uma mensagem é retornanda inforando que o palpite do usuário é número muito grande

if count >= math.log(maior_valor - menor_valor + 1,2): # se o valor da varável count for maior do que o número de tentativas
    print("\nO número é %d"% x) # o número é revelado
    print("\tMais sorte da próxima vez") # e uma mensagem para continuar tentando é retornada
