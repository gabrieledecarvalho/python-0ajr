#coding:utf-8
import math as m
print("Cálculo das soluções de uma equação do segundo grau: ")

#calculando de uma forma que não é eficiente para ver que usa complex numbers
coef_a1=1
coef_b1=0
coef_c1=4

delta1=coef_b1**2-4*coef_a1*coef_c1
x11=(-coef_b1+delta1**0.5)/(2*coef_a1) # quando se usa ** ele já está usando números complexos
x12=(-coef_b1-delta1**0.5)/(2*coef_a1) # vai sair em j (complex) mas não vai dar erro

print("Soluções: x1= ", x11, ", x2= ", x12)

#calculando de forma otimizada e com input do teclado
coef_a2=int(input("Digite o coeficiente a: "))
coef_b2=int(input("Digite o coeficiente b: "))
coef_c2=int(input("Digite o coeficiente c: "))

delta2=m.pow(coef_b2,2)-4*coef_a2*coef_c2
x21=(-coef_b2+m.sqrt(delta2))/(2*coef_a2) # vai dar erro caso delta for negativo
x22=(-coef_b2-m.sqrt(delta2))/(2*coef_a2)
print("Soluções: x1= ", x21, ", x2= ", x21)
