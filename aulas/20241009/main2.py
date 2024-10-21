# -*- coding: utf-8 -*-

#def calculaMedia(x1,x2,x3):
   # return (x1*2+x2*3+x3*5)/10

a = float(input())
b = float(input())
c = float(input())

media=(a*2+b*3+c*5)/10
#media=calculaMedia(a,b,c)

saida = "MEDIA = {0:.1f}".format(media)
print(saida)