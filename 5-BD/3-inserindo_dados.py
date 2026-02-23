import sqlite3

# 1 - Conectando no BD
connection = sqlite3.connect('title.db') # O connect tem duas funções, se o banco de dados não esxistir ele cria se existir ele conecta ao banco de dados

# 2 - Criando um cursor
'''
Cursor é um interador que permite navegar e manipular os registros em um DB
'''

cursor = connection.cursor()

# 3 - Inserindo Dados
cursor.execute("""
    INSERT INTO movies (name, year, score)
    VALUES ('Super Mario Bros', 2023, 10)
               """)

cursor.execute("""
    INSERT INTO movies (name, year, score)
    VALUES ('Avatar', 2023, 9.5)
               """)

cursor.execute("""
    INSERT INTO movies (name, year, score)
    VALUES ('Velozes e Furiosos', 2023, 8)
               """)

# 4 - Gravando Dados no BD
connection.commit()
print("Dados Inseridos com Sucesso")

# 5 - Fechando conexão
connection.close()