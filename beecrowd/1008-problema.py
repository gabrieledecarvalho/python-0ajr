# -*- coding: utf-8 -*-
# calcula salario de funcionário
numeroFuncionario = int(input())
numeroHorasTrabalhadas = int(input())
valorHora = float(input())
salario = numeroHorasTrabalhadas*valorHora
print("NUMBER =",numeroFuncionario)
print("SALARY = U$ {0:.2f}".format(salario))