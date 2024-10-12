# -*- coding: utf-8 -*-
# distância entre dois pontos
px1, py1 = input().split()
px2, py2 = input().split()

px1=float(px1)
py1=float(py1)
px2=float(px2)
py2=float(py2)

distancia = pow((pow((px2-px1),2)+pow((py2-py1),2)),0.5)
print("{:.4f}".format(distancia))