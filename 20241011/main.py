#coding: utf-8

def script1():
    #lista = list(range(6,13))
    for i in range(6,18,2):
        print(i)
        # print (lista)

def script2():
    soma = 0
    quantidade = 0
    n = float(input("Entre com o valor inicial de n: "))
    while(n!=0):
        soma+=n
        quantidade = quantidade + 1 #quantidade+=1
        n = float(input("Entre com um valor para n, zero para sair: "))
    else:
        print("Entrada no else")
        print(f"Soma = {soma} e quantidade = {quantidade}")
    print("(Media = {:.2f})".format(soma/quantidade))


if __name__=="__main__": # início do código
    #script1()
    script2()