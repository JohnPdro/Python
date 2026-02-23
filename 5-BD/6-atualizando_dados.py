import sqlite3

# 1 - Conectando no BD
connection = sqlite3.connect('title.db') # O connect tem duas funções, se o banco de dados não esxistir ele cria se existir ele conecta ao banco de dados

# 2 - Criando um cursor
'''
Cursor é um interador que permite navegar e manipular os registros em um DB
'''

cursor = connection.cursor()

# 3 - Solicitando Dados do Usuário
id = int(input("Informe o id do filme que deseja atualizar\n"))
name = input("Informe o novo nome do filme\n")

#4 - Atualizando Dados
cursor.execute("""
    UPDATE movies SET name = ?
    WHERE id = ?
               """, (name, id)) 

# 5 - Atualizando Dados no BD
connection.commit()
print("Dados Atualizados com Sucesso")

# 6 - Fechando conexão
connection.close()