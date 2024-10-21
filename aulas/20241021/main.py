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
    vetScript02.remove(3.4)
    print(vetScript02)
    #   removendo todos os A dentro do vetor, com while
    print("Escolha a remoção do A: ")
    escolha = input("Pressione 1 para remover a primeira ocorrência, outra tecla (alfanumérica) para todas: ")
    if 'A' in vetScript02:
        if(escolha == '1'):
            vet.remove('A') # é uma forma lenta de fazer a remoção
        else:
            while 'A' in vetScript02:
                vet.remove('A')
    print("Vetor final: ", vetScript02)

# função que remove elementos por posição:
def script03(vetScript03):
    print("Vetor recebido: ", vetScript03)
    posicaoFinalVetor = len(vetScript03) -1
    print(f"Digite a posição que você quer remover do vetor, entre 0 e {posicaoFinalVetor}") #format simplificado
    pos = int(input())
    del vetScript03[pos]
    print(f"Vetor com posição {pos} removida ", vetScript03)

# funçao que concatena listas
def script04():
    valores = list(range(1,11))
    anos = list(range(2020,2060,10))
    listaConcatenada = valores+anos
    print(valores)
    valores.extend(anos) #colocando a lista anos no final de valores
    print(valores)
    print(listaConcatenada)

# função que utiliza o sort
def script05():
    gatos = ['misa', 'laurel', 'kyra', 'wandy', 'olivia']
    print(gatos)
    gatos.sort()
    print(gatos)
    cachorros = ['luciana', 'Bonnie']
    cachorros.sort(key = str.casefold)
    print(cachorros)

if __name__=="__main__": # não esquecer dessa linha
    # chamando a funçao script01()
    vet = script01()
    print(vet)

    # chamando a função script02()
    script02(vet)

    # camando a funçaõ script03()
    script03()

    script04()