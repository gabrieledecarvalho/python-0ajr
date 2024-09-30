# coding utf-8
import math as m 
print("Script para resolver equação de 2º grau.")

def equacao2grau():
    coeficiente_a = int(input("Entre com o coeficiente a da equação: ")) # variavel int consome menos memória
    coeficiente_b = int(input("Entre com o coeficiente b da equação: "))
    coeficiente_c = int(input("Entre com o coeficiente c da equação: "))

    delta = m.pow(coeficiente_b,2)-4*coeficiente_a*coeficiente_c # se eu uso pow ele converte automático para float
    print(delta)

    x1 = (-coeficiente_b+m.sqrt(delta))/2*coeficiente_a
    x2 = (-coeficiente_b-m.sqrt(delta))/2*coeficiente_a

    print("Primeira solução: ", x1)
    print("Primeira solução: ", x1)

equacao2grau()
print("linha 20")