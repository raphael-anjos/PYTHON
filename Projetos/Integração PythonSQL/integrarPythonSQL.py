import pyodbc
import pandas as pd
server = '127.0.0.1'
database = 'PontoDasAguas'
driver = '{SQL Server}' # Driver you need to connect to the database


conexao = pyodbc.connect('DRIVER='+driver+';SERVER='+server+';DATABASE='+database+'')
print("Conexão estabelecida com sucesso.")

tabela = pd.read_sql_query('SELECT * FROM Vendas',conexao)
print(tabela)