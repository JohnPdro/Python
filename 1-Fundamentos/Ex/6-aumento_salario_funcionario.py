salario = float(input("Digite o valor do seu salário\n"))

if salario > 1250.00 :
    aumento = (salario / 100) * 10
else :
    aumento = (salario / 100) * 15
    
print(f"O aumento é de R${aumento} e o salario mais o aumento é R${salario + aumento:.2}") 


### Outra possível forma de realizar ###
# salario = float(input("Digite o valor do seu salario"))
# perc_increase = 0.15

# if salario > 1250 :
#     perc_increase = 0.10
    
# aumento = salario * perc_increase
# print(f"O aumento é de R${aumento} e o salario mai o aumento é R${salario + aumento:.2f}")