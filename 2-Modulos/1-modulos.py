import mod.calc  # Neste caso estou importando o modulo por completo 
from mod.calc import div # Neste caso estou importando apenas uma função pertencente ao modulo calc

print(mod.calc.soma(1, 4)) # Utiliza a chamada completa pois foi realizada a importação de todo o modulo calc
print(mod.calc.sub(1, 4))
print(mod.calc.div(1, 4))
print(mod.calc.mult(1, 4))

print(div(1, 4)) # Quando importamos uma função do modulo não precisamos fazer a chamada completa utilizamos apenas o nome da função pertencente ao modulo