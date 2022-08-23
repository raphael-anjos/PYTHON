import random

name_user = input("Digite seu nome: ") # Usuário entra com Nome
print('Boa sorte %s !'%name_user) # Mensagem para o usuário

# Função que vai ler uma série de palavras em um arquivo texto e armazenar em uma estrutura de lista
def palavra_secreta():
    palavras = [] # criando lista
    with open("lista_palavra.txt","r", encoding="utf-8") as arquivo: # realizando leitura do arquivo
        for linha in arquivo:
            linha = linha.strip() # removendo espaços no inicio e fim de cada linha do arquivo
            palavras.append(linha) # adicinando as palavras contidas no arquivo na lista
    palavra = random.choice(palavras) # Pegando uma palavra aleatória para dar inicio ao jogo
    return palavra

palavra = palavra_secreta() # Invocando método com a palavra aleatória já escolhida

palpites = '' # string que vai armazenar letra por letra cada palpite do usuário
tentativas = 10 # número de tentativas

while tentativas > 0:
    falhas = 0
    for letra in palavra:
        if letra in palpites: # se a letra que usuário inseriu como palpite fizer parte da palavra
            print(letra, end="") # a letra será impressa
        else:
            print('_', end="") # se não o programa vai continuar exibindo "_" pois o palpite da letra esta incorreto
            falhas+=1 # conta o número de falhas
    
    if falhas == 0: # Se usuário acertou todos os palpites
            print("\n\nVocê venceu !") # Mensagem de vitória
            print("A palavra é: %s"%palavra) # palavra é revelada ao usuário
            break # fim da estrutura pois a condição já foi satisfeita
    letra = input('\n\nInforme uma letra: ') # usuário informa uma letra como palpite
    if letra in palpites: # se a letra já tiver sido informada e concatenada a string palpites
        print("\nEssa letra já foi um palpite !") # o usuário recebe uma mensagem que aquela letra já foi um palpite
        letra = input('\n\nInforme outra letra: ') # e usuário deve informar outra letra
    else: 
        palpites+=letra # a letra é concatenada a string palpites

    if palpites not in palavra: # se a letra informada pelo usuário estiver errada e não fizer parte da palavra
        tentativas-=1 # numero de tentativas diminui
        print("\nVocê errou !") # mensagem de erro para o usuario
        print("\nVocê ainda tem ",tentativas,"para adivinhar a palavra")  # mensagem com numero de tentativas restantes        
        
    if tentativas == 0: # se numero de tentativas chegar a zero
        print("Você perdeu.") # mensasgem para usuario informando que ele perdeu
        print("\n\nA palavra era: %s"%palavra) # a palavra secreta é revelada    
    
