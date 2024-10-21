#coding: utf-8

def insercaoDadoVetor():
    vC = [1, 3.4, 'A', " IFSC "]
    print("Vetor Original: ", vC)
    #input("Digite enter para prosseguir: ")
    vC.insert(0,56) # adiciona na posição 0 o inteiro 56
    print("Adicionando o inteiro 56 na posição 8: ", vC)
    #input("Digite enter para prosseguir: ")
    vC.insert(3, 'B') # adiciona na posição 3 o caracter B
    print("Adicionando o caracter B na posição 3: ", vC)
    #input("Digite enter para prosseguir: ")
    vC.append(11) # adiciona no final do vetor, independente do número de posição, o inteiro 11
    print("Forma do vetor final em coluna: ", vC)
    #input("Digite enter para prosseguir: ")
    for i in vC: # printa o vetor vC em forma de coluna
        print(i)
    print("Fim da função inserção de dados no vetor!")
    return vC

def remocaoDadoVetor(vet):
    print("Vetor recebido: ", vet)
    print("Elemento 'A' removido")
    vet.remove('A')
    print("Vetor alterado: ", vet)
    input("Digite enter para prosseguir: ")

    print("Fim da função que remove elemento")

if __name__ == "__main__":
    vet = Insercao_dado()
    remocaoDadoVetor(vet)
    
    print("Fim do programa!") # monsta a mensagem no final do programa que o fim do programa chegou