# -*- coding: utf-8 -*-
# cálculo simples
def calculaValorTotalPeca():
    codigoDaPeca, numeroDePecas, valorUnitarioDaPeca = input().split
    codigoDaPeca = int(codigoDaPeca)
    numeroDePecas = int(numeroDePecas)
    valorUnitarioDaPeca = float(valorUnitarioDaPeca)
    total = numeroDePecas*valorUnitarioDaPeca
    return total

totalValor1 = calculaValorTotalPeca()
totalValor2 = calculaValorTotalPeca()
totalPagar = totalValor1 + totalValor2

print("VALOR A PAGAR: R$ {0:.2f}".format(totalPagar))

