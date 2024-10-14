#coding: utf-8
# programa que classifica feedbacks
n = int(input()) #numero de casos de teste 1 a 100
k = int(input()) #numero de feedbacks do dia 1 a 50

for i in range(n):
    for j in range (k):
        categoria = int(input())
        if(categoria==1):
            print("Rolien")
        if(categoria==2):
            print("Naej")
        if(categoria==3):
            print("Elehcim")
        if(categoria==4):
            print("Odranoel")
