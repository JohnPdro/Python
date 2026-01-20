gameName = "Fifa 23"
gameDescription = """
Fifa 23 é um jogo de futebol
desenvolvido pela EA Sports
e que possibilita jogar localmente ou online
"""

# string[início:fim] - índice começa na posição 0 | índice final -1

# 1 - Busque toda string a partir da primeira posição
print(gameName[0:])

# 2 - Busque toda string até a última posição
print(gameName[:7])

# 3 - Busque toda string na terceira até a última posição
print(gameName[2:])

# 4 - Busque toda a string de 2 em 2 caracteres
print(gameName[::2])

# 5 - Busque toda a string nos índices ímpares
print(gameName[1::2])

# 6 - Inverter uma strig de trás para frente
print(gameName[::-1])