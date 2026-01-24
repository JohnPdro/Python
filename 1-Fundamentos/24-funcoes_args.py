"""
*args - Utilizamos ele quando não temos ceteza de quantos argumentos queremos ter numa função.
-Os argumentos são passados como uma tupla

**kwargs - Além dos valores podemos passar também as respectivas chaves para cada argumento 
- Os argumentos são passados como um dicionário
"""

# 1 - Soma de números 
def sum(*num) :
    sum_total = 0 
    for n in num :
        sum_total += n # sum_total = sum_total + n
    print(f"Soma é: {sum_total}")
    
sum(7)
sum(7,9)
sum(7, 9, 10, 11)
sum(7, 10, 9, 8, 7, 6)

# 2 - Apresentação de cursos
def presentation(**data) :
    for key, value in data.items() :
        print(f"{key} - {value}")
presentation(name = "Python", category = "Backend", level = "Iniciante")
presentation(name = "Visão Computacional com Python", category = "Data Science", level="Intermediário") 