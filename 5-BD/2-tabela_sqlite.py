import sqlite3

# 1 - Conectando no BD
connection = sqlite3.connect('title.db') # O connect tem duas funções, se o banco de dados não esxistir ele cria se existir ele conecta ao banco de dados

# 2 - Criando um cursor
'''
Cursor é um interador que permite navegar e manipular os registros em um DB
'''

cursor = connection.cursor()

# 3 - Criando a Tabela
cursor.execute("""
    CREATE TABLE movies(
      id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
      name TEXT NOT NULL,
      year INTEGER NOT NULL,
      score REAL NOT NULL  
    );
               """)

# 4 - Fechando a conexão
print("Tabela criada com sucesso")
connection.close()