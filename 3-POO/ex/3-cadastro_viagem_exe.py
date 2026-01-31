from cadastro_viagem_3 import Trip

trip0 = Trip("Lenóis Maranhense")
trip1 = Trip("Florinópolis")
trip2 = Trip("Gramado")
trip3 = Trip("Campos do Jordão")
trip4 = Trip("Caldas Novas")

print("E aí viajante. Temos algumas ofertas para você.")
traveler = input("Digite o seu nome para começar\n")
print(f"{traveler} temos 5 destinos que combinam com você"
      """
        [0] - Lencóis Maranhese
        [1] - Florianópolis
        [2] - Gramado
        [3] - Campos do Jordão
        [4] - Caldas Novas
      """
      )
choice = int(input("Selecione o destion da viagem\n"))
list_trip = [trip0, trip1, trip2, trip3, trip4]

for option in list_trip :
    if choice >= 5 :
        print("Esta opção não está incluída em nosso destinos")
        break
    else :
        print(f"{traveler} sua viagem para {list_trip[choice].destiny} estámarcada")
        print("Boa Viagem!")
        break
