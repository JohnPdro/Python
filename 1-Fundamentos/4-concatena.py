name = input("Digite o nome do jogo\n")
yearLaunch = int(input("Digite o ano de lançamento\n"))
gamePrice = float(input("Digite o valor do jogo\n"))
planIncluded = input("Está incluso no serviço mensal?\n")

print("==============")
# Alternativa 1
print("Nome do Jogo:", name)
print("Ano do Jogo:", yearLaunch)
print("Preço do Jogo:", gamePrice)
print("Está incluído no plano?", planIncluded)

print("==============")
# Alternativa 2
print("Nome do Jogo:", name, "\nAno de lançamento:", yearLaunch, "\nPreço do Jogo:", gamePrice, "\nEstá incluso no serviço?", planIncluded)

print("==============")
# Alternativa 3
print(f"Nome do Jogo: {name} \nAno de lançamento: {yearLaunch} \nPreço do Jogo: {gamePrice} \nEstá incluso no serviço? {planIncluded}")