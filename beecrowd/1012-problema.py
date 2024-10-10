# -*- coding: utf-8 -*-
A, B, C = input().split()
A = float(A)
B = float(B)
C = float(C)
constantePi = 3.14159
areaTriangulo = A*C/2
areaCirculo = constantePi*pow(C,2)
areaTrapezio = ((A+B)*C)/2
areaQuadrado = pow(B,2)
areaRetangulo = A*B
print("TRIANGULO: {0:.3f}".format(areaTriangulo))
print("CIRCULO: {0:.3f}".format(areaCirculo))
print("TRAPEZIO: {0:.3f}".format(areaTrapezio))
print("QUADRADO: {0:.3f}".format(areaQuadrado))
print("RETANGULO: {0:.3f}".format(areaRetangulo))