# coding utf-8
import math as m
import numpy as np

print("Script para resolver equação de 2º grau.")

def equacao2grau(): # iniciando uma função
    coeficiente_a = a #utilizando outro nome de variavel que só existe aqui na funcao
    coeficiente_b = b
    coeficiente_c = c

    delta = m.pow(coeficiente_b,2)-4*coeficiente_a*coeficiente_c # se eu uso pow ele converte automático para float
    print(delta)

    x1 = (-coeficiente_b+m.sqrt(delta))/2*coeficiente_a
    x2 = (-coeficiente_b-m.sqrt(delta))/2*coeficiente_a
    
    return x1,x2

#utilizando numero aleatorio
for i in range(50)
    print("Equação ", i+1)
    a = np.randint(1,15)
    b = np.randint(1,15)
    c = np.randint(1,15)
    sol1, sol2 = equacao2grau(a,b,c)
    

'''
a = int(input("Entre com o coeficiente a da equação: ")) # variavel int consome menos memória
b = int(input("Entre com o coeficiente b da equação: "))
c = int(input("Entre com o coeficiente c da equação: "))

sol1,sol2=equacao2grau(a,b,c)

print("Primeira solução: ", sol1)
print("Primeira solução: ", sol2)
'''

# equacao2grau()
print("linha 20")

#gravar esse arquivo em saída.dat e ele pega todas as saídas e grava em um arquivo