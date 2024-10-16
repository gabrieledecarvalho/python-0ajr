#coding: utf-8
# usando entrada externa, problema do beecrowd

# 1a forma:
def forma1Leitura():
    vet = input().split()
    tamanho_vet = len(vet)
    for i in range(tamanho_vet):
    #for i in range(len(vet)): # sem a variável tamanho_vet
        vet = int(vet[i])
    print(vet)

#2a forma - equivalente à primeira
def forma2Leitura():
    vet = map(int,input().split())
    #print(vet)

    #código não otimizado, melhor com array
    tamanho_vet = len(vet)
    for i in range(tamanho_vet):
        #vet[i] = 3*vet[i]
        vet[i]*=3
        print(vet[i],end =' ') # substituindo o enter por espaço no end
    print()

# 3a forma, mais otimizada
import array

def forma3LeituraArray():
    vet = array.array('i', map(int, input().split())) # map transforma o input split em caracter
    tamanho_vet = len(vet)
    for i in range(tamanho_vet):
        vet[i]*=3
        print(vet[i], end = " ")
    print()

if __name__ == "__main__":
    #forma1Leitura()
    #forma2Leitura()
    forma3LeituraArray()