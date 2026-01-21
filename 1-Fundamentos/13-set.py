gamesSet = {"Resident Evil4", "Red Dead 2", "Skate 3", "COD4"}
print(gamesSet)

# 1 - Buscar o tamanho do set
print(len(gamesSet))

# 2 - True e 1 são considerados o mesmo valor
exempleSet = {"Fifa 23", True, 1, 90.50}
print(exempleSet)

# 3 - Adicionar item de outro set
gamesSet.update(exempleSet)
print(gamesSet)

# 4 - Remover um item no set
gamesSet.remove(True)
gamesSet.remove(90.50)
print(gamesSet)


# Não possibilita recuperar valores via fatiamento ou slice
# Não possibilita repetir valores