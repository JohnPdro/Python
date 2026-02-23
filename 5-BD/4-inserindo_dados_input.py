import sqlite3

# 1 - Conectando no BD
connection = sqlite3.connect('title.db') # O connect tem duas funções, se o banco de dados não esxistir ele cria se existir ele conecta ao banco de dados

# 2 - Criando um cursor
'''
Cursor é um interador que permite navegar e manipular os registros em um DB
'''

cursor = connection.cursor()

# 3 - Solicitando Dados do Usuário
name = input("Nome do Filme\n")
year = int(input("Ano do Filme\n"))
score = float(input("Nota do Filme\n"))

# 4 - Inserindo Dados
cursor.execute("""
    INSERT INTO movies (name, year, score)
    VALUES (?, ?, ?)
               """, (name, year, score))

# 5 - Gravando Dados no BD
connection.commit()
print("Dados Inseridos com Sucesso")

# 6 - Fechando conexão
connection.close()