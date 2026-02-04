name = input("Digite o seu nome:\n")
"""
- Arquivos:
1 - opção w - write (Subscreve o que está escrito)
2 - opção a - append (Escreve no final)
3 - opção r - read (Lê dados de um arquivo)
"""
# Alternativa 1
# file = open("names.txt", "w")
# file.write(f"{name}\n")
# file.close()

# Alternativa 2
with open("names.txt", "a") as file :
    file.write(f"{name}\n")
    
# with open("names.txt", "a") as file - Significado da linha - 
# “Utiliza um gerenciador de contexto para abrir o arquivo 
# names.txt em modo append, associando-o à variável file.”

# O gerenciador de contexto é a tag with, ela serve para:
# abrir arquivo
# usar arquivo
# fechar o arquivo 
# Tudo isso de forma automatica
