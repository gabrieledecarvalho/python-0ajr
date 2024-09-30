#coding utf-8
import math
# revisão entrada e saída de dados


print("Olá mundo!") # respeitando a história da programação e começando com o Olá mundo!

print("Resolvendo uma equação de 2º grau: ")

a = 1 # pode colocar o espaço ou não
b=4
c=3

delta = b** - 4*a*c # criando uma variável delta
x1=(-b+delta*0.5)/2*a # resolvendo o x1
x2=(-b-delta*0.5)/2*a # resolvendo o x2

# x2=(-b-math.sqrt(delta))/2*a 

print("O valor de x1 é: ",x1)
print("O valor de x2 é: ",x2)
