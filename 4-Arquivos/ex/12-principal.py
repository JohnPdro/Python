from agenda import add_contact, view_contacts, delete_contacts

def main() :
    while True :
        print("\nAgenda de Contatos")
        print("1. Adicionar Contato")
        print("2. Lista Contato")
        print("3. Remover Contato")
        print("4. Saie")
        
        choice = input("Escolha a opção (1-4)\n")
        if choice == "1" :
            add_contact()
        elif choice == "2" :
            view_contacts()
        elif choice == "3" :
            delete_contacts()
        elif choice == "4" :
            break
        else :
            print("Informe uma opção válida")

main()
