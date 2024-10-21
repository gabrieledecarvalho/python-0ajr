#coding: utf-8

def script1(): #mostra uma lista na tela
    #lista = list(range(6,13))
    for i in range(6,18,2):
        print(i)
        # print (lista)

def script2(): #mostra a média
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

def script3(): # se numero menor que 10, mostra os sucessores e quantidade de sucessores
    n = int(input("Digite um número menor do que 10: "))
    
    while(n>=10): #n>9
        n=int(input("Por favor, digite um número menor que 10: "))
    
    quantidade = 0
    i=n
    
    while (i<20):
        i+=1
        print(i)
        quantidade+=1
    else:
        print("Total de sucessores = ",quantidade)

def script4(): # se numero menor que 10, mostra os sucessores e quantidade de sucessores, mudando o while teste se n < 10
    flag = False
    while True:
        if flag == True:
            break
        n = int(input("Digite um número menor do que 10: "))
        if (n<10):
            flag = True
            contador = 0
            while(n<20):
                n+=1
                print(n)
                contador += 1
            else:
                print(f"Total de sucessores = {contador}")
        else:
            print("O número tinha que ser menor do que 10.")

if __name__=="__main__":
    script3()

if __name__=="__main__": # início do código
    #script1()
    #script2()
    script3()
    #script4()