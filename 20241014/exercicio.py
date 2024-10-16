#coding: utf-8
# não sei qual é esse exercício do beecrowd
# Crie um programa que leia uma linha contendo vários números inteiros
# separados por espaço, armazene em um vetor e altere cada elemento
# multiplicando o mesmo por 3. Por fim, imprima cada elemento multiplicado
# por 3 em uma linha e separados por espaço



entrada = input()
vetor = []
vetor = entrada.split(" ")

for i in range(len(entrada)):
    vetor[i] = vetor[i]*3

print(vetor)