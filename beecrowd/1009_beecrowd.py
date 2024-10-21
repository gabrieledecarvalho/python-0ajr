# -*- coding: utf-8
# calcula salário com bônus
nomeVendedor = input()
salarioFixoVendedor = float(input())
valorTotalVendasEfetuadasMes = float(input())
comissao = 0.15
valorTotalReceber = valorTotalVendasEfetuadasMes*comissao + salarioFixoVendedor
print("TOTAL = R$ {0:.2f}".format(valorTotalReceber))