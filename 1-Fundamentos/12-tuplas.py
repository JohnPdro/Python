gamesTuple = ("Resident Evil4", "Red Dead 2", "Skate 3", "COD4")

print(gamesTuple)
print(type(gamesTuple))

# 1 - Buscar os dois primeiros itens da tupla
print(gamesTuple[:2])

# 2 -  Buscar o último item da lista
print(gamesTuple[-1])

# 3 - Buscar jogos até uma determinada posição
print(gamesTuple[:3])

# 4 - Buscar jogos de uma posição em diante
print(gamesTuple[2:])

# 5 - Recuperar um item da tupla pelo índice
print(gamesTuple.index("Red Dead 2"))

# Não possibilita adicionar valores na tupla
# Não possibilita remover valores na tupla
# Não possibilita ordenar valores na tupla