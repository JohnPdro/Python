name = input("Digite o nome do jogo\n")

char = name[0].lower()
new_name = name.replace(char, '$')
new_name = char.upper() + new_name[1:]
print(new_name)