import requests
import json
def buscar_cep():
    cep = input('Informe apenas o número do CEP: ')
    request = requests.get(f"https://viacep.com.br/ws/{cep}/json/")
    retorno = json.loads(request.content)
    #print(retorno)
    rua = retorno['logradouro']
    bairro = retorno['bairro']
    print("Rua: {}\nBairro: {}".format(rua, bairro))


if __name__ == '__main__':
    buscar_cep()