#coding: utf-8

def comissaoSalario(): #funçao
    nome = input("Entre com o nome do vendedor: ")
    salarioFixo = float(input("Informe o salario: "))
    vendas = float(input("Informe o valor total em vendas: "))
    comissao = 0.15*vendas
    pagamentoTotal = salarioFixo+comissao
    return nome, comissao, pagamentoTotal

if __name__=="__main__":
    nome, comissao, pagamentoTotal = comissaoSalario() 
    
    strg = "{0} obteve R$ {1:.2f} de comissão e vai receber {2:.2f} no total.".format(nome, comissao, pagamentoTotal)
    print(strg)