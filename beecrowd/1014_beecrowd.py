# -*- coding: utf-8 -*-
X = int(input()) # distância total percorrida em km
Y = float(input()) # total de combustível gasto

consumoMedio = X/Y # consumo médio quilometro / litro
print("{0:.3f} km/l".format(consumoMedio))
