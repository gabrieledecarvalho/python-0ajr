#coding utf-8
import math as m #criando um apelido para a biblioteca
# revisão entrada e saída de dados


print("Olá mundo!") # respeitando a história da programação e começando com o Olá mundo!

print("Resolvendo uma equação de 2º grau: ")

a = 1 # pode colocar o espaço ou não
b=4
c=3

#método mais otimizado:
delta = m.pow(b,2)-4*a*c
x1=(-b+m.sqrt(delta))/2*a
x2=(-b-m.sqrt(delta))/2*a

'''
delta = b**2-4*a*c # criando uma variável delta
x1=(-b+delta*0.5)/2*a # resolvendo o x1 de forma lenta pois não usa funções
x2=(-b-delta*0.5)/2*a # resolvendo o x2
'''

''' 
x2=(-b-math.sqrt(delta))/2*a 
como criei um apelido para a biblioteca math então a linha acima fica como:
x2=(-b-m.sqrt(delta))/2*a 

a forma mais otimizada para fazer essa equação é utilizar o pow:
delta = m.pow(b,2)-4*a*c #boa prática de programação
'''

print("O valor de x1 é: ",x1)
print("O valor de x2 é: ",x2)
