#coding: utf-8
# programa que ajuda o Og a contar suas crianças
soma = 0
while True:
    l,r = input().split()
    l = int(l)
    r = int(r)
    if (l==0 and r == 0):
        break
    else:
        soma = l + r
        print(soma)
    
