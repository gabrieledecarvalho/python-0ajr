#coding: utf-8

# função que adiciona elementos no vetor, em posições específicas e no final
def script01():
    vC = [1, 3.4, 'A', " IFSC "]
    vC.insert(0,56)
    vC.insert(3, 'B')
    vC.append(11)
    vC.append('A')
    return vC

# função que remove elementos do vetor
def script02(vetScript02):
    print("Vetor recebido: ",vetScript02)
    vetScript02.remove('A') # não precisa fazer vetScript02 = vetScript02.remove('A')
    vetScript02.remove(3.4)
    print(vetScript02)

if __name__=="__main__": # não esquecer dessa linha
    # chamando a funçao script01()
    vet = script01()
    print(vet)

    # chamando a função script02()
    script02(vet)