"""
- Arquivos:
1 - opção w - write (Subscreve o que está escrito)
2 - opção a - append (Escreve no final)
3 - opção r - read (Lê dados de um arquivo)
"""

with open("dados/names.txt", "r", encoding = "utf-8") as file :
    for line in file :
        print(f"Olá, {line.rstrip()}") 