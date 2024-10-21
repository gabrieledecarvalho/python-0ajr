#coding: utf-8
#12 KM/L
tempoViagem = int(input()) #em horas
velocidadeMedia = int(input()) #em km/h

distancia = velocidadeMedia*tempoViagem #km

litrosGastos = distancia/12 #litros
print("{0:.3f}".format(litrosGastos))