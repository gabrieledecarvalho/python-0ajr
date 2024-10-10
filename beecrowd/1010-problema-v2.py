# -*- coding: utf-8 -*-
# cálculo simples

codigoDaPeca1, numeroDePecas1, valorUnitarioDaPeca1 = input().split()
codigoDaPeca2, numeroDePecas2, valorUnitarioDaPeca2 = input().split()

codigoDaPeca1 = int(codigoDaPeca1)
codigoDaPeca2 = int(codigoDaPeca2)

numeroDePecas1 = int(numeroDePecas1)
numeroDePecas2 = int(numeroDePecas2)

valorUnitarioDaPeca1 = float(valorUnitarioDaPeca1)
valorUnitarioDaPeca2 = float(valorUnitarioDaPeca2)

totalPagar = numeroDePecas1*valorUnitarioDaPeca1 + numeroDePecas2*valorUnitarioDaPeca2
print("VALOR A PAGAR: R$ {0:.2f}".format(totalPagar))