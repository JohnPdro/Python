gamesList = ["Fifa", "God of War", "Red Dead 2", "Uncharted"]

# 1 - Iterando valores de uma lista
for game in gamesList :
    print(game)
    
# 2 - Quando a condição for atendida, o loop será encerrado
for game in gamesList : 
    if game == "Red Dead 2" :
        break
    print(game)

# 3 - Quand a condição for atendida, o loop vai para a próxima iteração
for game in gamesList : 
    if game == "Red Dead 2" : 
        continue
    print(game)
    
# 4 - Avaliação do Jogo
gameName = input("Digite o nome do jogo\n")
gameRating = int(input("Digite quantas avaliações deseja fazer no jogo\n"))

sum = 0
for i in range(gameRating) : 
    note = float(input("Digire a nota para o jogo\n"))
    sum += note # sum = sum + note
print(f"Média de avaliação do jogo {gameName} é {sum / gameRating :.2f}")