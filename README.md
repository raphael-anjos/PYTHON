# Lista de exercicios e projetos em Python

[Lista de Exercícios](https://wiki.python.org.br/ListaDeExercicios "Lista de Exercícios")

## Praticando com Python

Neste repositório contém a resolução de uma lista exercicios utilizando a linguagem Python, os arquivos que contém a palavra **"extra"** são melhorias que desenvolvi com base na necessidade que encontrei no exercicio proposto.

## Exemplo: 
 Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês. 
### Resolução do exercicio:
 ```python
valor_hora = float(input('Quanto você ganha por hora trabalhada? '))
hora_trabalho_mes = int(input('Quantas horas você trabalha por mês? '))
hora_salario = valor_hora * hora_trabalho_mes
print('Seu salário em um mês é de:', hora_salario)
```
### Melhoria:
Descobrir o valor da hora trabalhada com base no salário:
```python
salario = float(input('Informe seu salario: '))
hora_trabalho = int(input('Informe as horas trabalhadas durante o mês: '))
dias_trabalho = int(input('Informe a quantidade de dias trabalhados no mês:'))


valor_hora = salario / dias_trabalho / hora_trabalho

print('Seu valor por hora trabalhada é:', valor_hora)
```

## Projetos

Adicionei também dois projetos que havia realizando em Python, um deles é um algoritmo de caixa eletrônico que executa operações de depósito e saque.
### Caixa eletrônico
O algoritmo inicia perguntando ao usuário qual operação ele deseja realizar, caso ele selecione a operação de saque e for um novo correntista ele receberá uma mensagem de que precisa ativar sua conta realizando um depósito de qualquer valor. Realizando o depósito ele consegue seguir com o saque.
Para cada operação (depósito/saque) é exibido o saldo em conta, na operação de saque caso o valor seja aprovado também é exibido a contagem de cédulas.

Outro projeto que adicionei foi uma tela de login.
### Tela de Login
Utilizando o tktinter conseguir criar uma interface para uma tela de login com conexão a uma base de dados, então os usuários podem se cadastrar e em seguida informar seu nome de usuário e senha que foram cadastrados, o acesso só será liberado caso os dados informados sejam válidos, para isso é realizada uma consulta em um banco de dados Sqlite.
Os usuários também tem a opção de redefinir sua senha em caso de esquecimento, para isso é só lembrar o e-mail que foi cadastrado e definir uma nova senha.
