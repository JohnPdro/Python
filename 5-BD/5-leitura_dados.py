import sqlite3

# 1 - Conectando no BD
connection = sqlite3.connect('title.db') # O connect tem duas funções, se o banco de dados não esxistir ele cria se existir ele conecta ao banco de dados

# 2 - Criando um cursor
'''
Cursor é um interador que permite navegar e manipular os registros em um DB
'''

cursor = connection.cursor()

# 3 - Lendo Dados da Tabela
data = cursor.execute("""
    SELECT name, year, score FROM movies 
                      """)

print(data.fetchall())

# 4 - Iterando os dados
for row in cursor.execute("SELECT * FROM movies") :
    print(f"{row}")
    
# 5 - Ordenando os Dados pelo score
for row in cursor.execute("SELECT * FROM movies ORDER BY score DESC") :
    print(f"{row}")

# 5 - Fechando conexão
connection.close()