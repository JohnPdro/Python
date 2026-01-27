import random

game = True

while game :
    print("======================")
    print("Escolha uma opção\n")
    print("1. Jogar")
    print("2. Sair")
    print("======================")
    choice = input(">")
    
    if choice == "1" :
        print("Adivinhe o número de 1 a 10")
        random_num = random.randint(1, 10)
        num = int(input(">"))
        if num == random_num :
            print("Parabéns você acertou o número\n")
        elif num < 1 or num > 10 :
            print("Número invalido\n")
        else :
            print("Número errado\n")
    elif choice == "2" :
        game = False
    else : 
        print("Opção inválida\n")
        
    