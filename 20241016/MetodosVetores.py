#coding: utf-8
def Insercao_dado():
    print("Vetor Original: ", vC)
    input("Digite enter para prosseguir: ")
    vC = [1, 3.4, 'A', " IFSC "]
    vC.insert(0,56) # adiciona na posição 0 o inteiro 56
    vC.insert(3, 'B')
    vC.append(11)
    for i in vC:
        print(i)

if __name__ == "__main__":
    Insercao_dado()