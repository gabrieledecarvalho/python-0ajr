#coding: utf-8
# mostra os divisores de um número lido pelo teclado
n=int(input())
i=1
while(i<n+1):
    if(n%i==0):
        print(i)
    i+=1