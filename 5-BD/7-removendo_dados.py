import sqlite3

# 1 - Conectando no BD
connection = sqlite3.connect('title.db') # O connect tem duas funções, se o banco de dados não esxistir ele cria se existir ele conecta ao banco de dados

# 2 - Criando um cursor
'''
Cursor é um interador que permite navegar e manipular os registros em um DB
'''

cursor = connection.cursor()

# 3 - Solicictando Dados do Usuário
id = int(input("Informe o id do filme que deseja remover\n"))

# 4 - Removendo Dados
cursor.execute("""
    DELETE FROM movies
    WHERE id = ?
               """, (id,)) # Como temos apenas o id dentro da tupla é necessário adicionar uma virgula após para informar que é um parametro da tupla

# 5 - Removendo Dados no BD
connection.commit()
print("Filme removido com Sucesso")

# 6 - Fechando conexão
connection.close()