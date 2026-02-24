from conexao_post import conn

# Cria um cursor
cursor_obj = conn.cursor()

# Executa uma query
cursor_obj.execute("SELECT * FROM game")

# Pega o resultado de todos os registros
result = cursor_obj.fetchall()

# Exibe o resultado
print(result)