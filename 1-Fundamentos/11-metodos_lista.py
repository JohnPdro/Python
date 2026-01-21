gamesList = ["Resident Evil4", "Red Dead 2", "Skate 3", "COD4"]

# 1 - Tamanho da Lista
print(len(gamesList))

# 2 - Recuperar um item da lista pelo índice
print(gamesList.index("Skate 3"))

# 3 - Adicionar item ao final da lista
gamesList.append("GTA V")
print(gamesList)

# 4 - Ordenar lista 
gamesList.sort()
print(gamesList)

# 5 - Copiar os itens de uma lista para outra
gameReset = gamesList.copy() # Copia de uma lista para outra 
gameReset.remove("COD4") # Remove item da lista
print(gameReset)

# 6 - Remove todos os itens da lista
gamesList.clear()
print(gamesList)