# -*- coding: utf-8 -*-

# programa que calcula o maior

def calculaMaior(a,b):
    maior = (a + b + abs(a-b))/2
    return maior

# recebendo informações em linha
x1, x2, x3 = input().split()

#convertendo as informações acima para int
x1 = int(x1)
x2 = int(x2)
x2 = int(x3)

maiorx1x2 = calculaMaior(x1,x2)
maiorx1x2x3 = int(calculaMaior(maior,x3))

print("{0} eh o maior", maiorx1x2x3)