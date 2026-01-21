distancia = float(input("Digite a distancia desejada em kilometros\n"))

if distancia > 200 :
    valorPassagem = distancia * 0.35
else :
    valorPassagem = distancia * 0.50
    
print(f"O valor a ser pago por {distancia} km percorrido é R${valorPassagem:.2f}")